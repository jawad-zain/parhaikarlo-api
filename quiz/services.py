from django.db import transaction
from django.utils import timezone
from .models import Attempt, AttemptQuestion
from content.models import Question
from .models import Attempt, AttemptQuestion
from content.models import Question


class QuizCreationError(Exception):
    """Raised when we can't build a valid attempt (e.g. not enough Qs in pool)."""
    pass


def select_questions_for_practice(user, exam, subject=None, topic=None, subtopic=None, difficulty=None, limit=20):
    """
    Pick questions for a practice session.
    MVP: random sample from filtered pool.

    A subtopic/topic-scoped pool is often smaller than `limit` — plenty of
    subtopics only have a handful of questions (see the syllabus click-
    through feature). Rather than 400 whenever a scoped pool is short,
    we serve whatever's available and only error out on a genuinely empty
    pool. Frontend also caps its requested `limit` client-side, but a
    bookmarked/shared deep link can still arrive with a stale/oversized
    limit, so this cap has to hold server-side regardless.
    """
    qs = Question.objects.filter(
        subtopic__topic__subject__exam=exam,
        is_active=True,
        is_verified=True,
    )
    if subject:
        qs = qs.filter(subtopic__topic__subject=subject)
    if topic:
        qs = qs.filter(subtopic__topic=topic)
    if subtopic:
        qs = qs.filter(subtopic=subtopic)
    if difficulty:
        qs = qs.filter(difficulty=difficulty)

    question_ids = list(qs.order_by('?').values_list('id', flat=True)[:limit])

    if not question_ids:
        raise QuizCreationError('No questions available for this selection.')
    return question_ids


@transaction.atomic
def create_practice_attempt(user, exam, subject=None, topic=None, subtopic=None, difficulty=None, limit=20, device_class='desktop'):
    """
    Create a practice Attempt + snapshot N AttemptQuestion rows in one DB transaction.
    """
    question_ids = select_questions_for_practice(
        user=user, exam=exam, subject=subject, topic=topic, subtopic=subtopic,
        difficulty=difficulty, limit=limit,
    )

    attempt = Attempt.objects.create(
        user=user,
        mode='practice',
        exam=exam,
        subject=subject,
        topic=topic,
        subtopic=subtopic,
        total_questions=len(question_ids),
        device_class=device_class,
    )

    AttemptQuestion.objects.bulk_create([
        AttemptQuestion(
            attempt=attempt,
            question_id=qid,
            order_in_attempt=idx + 1,
        )
        for idx, qid in enumerate(question_ids)
    ])

    return attempt


def finalize_attempt(attempt):
    """
    Called on submit. Computes total score, per-subject and per-topic
    breakdown, marks attempt completed, refreshes UserProgress.
    """
    if attempt.is_completed:
        raise QuizCreationError("Attempt already submitted")

    items = attempt.items.select_related(
        'question__subtopic__topic__subject'
    ).all()

    total = items.count()
    answered = items.exclude(selected_option__isnull=True).exclude(selected_option='').count()
    correct = items.filter(is_correct=True).count()

    subject_stats = {}
    topic_stats = {}

    for aq in items:
        subj = aq.question.subtopic.topic.subject.name
        topic = aq.question.subtopic.topic.name

        subject_stats.setdefault(subj, {'total': 0, 'correct': 0, 'answered': 0})
        subject_stats[subj]['total'] += 1
        if aq.selected_option:
            subject_stats[subj]['answered'] += 1
        if aq.is_correct:
            subject_stats[subj]['correct'] += 1

        topic_key = f"{subj} / {topic}"
        topic_stats.setdefault(topic_key, {'total': 0, 'correct': 0, 'answered': 0})
        topic_stats[topic_key]['total'] += 1
        if aq.selected_option:
            topic_stats[topic_key]['answered'] += 1
        if aq.is_correct:
            topic_stats[topic_key]['correct'] += 1

    for stats in subject_stats.values():
        stats['accuracy_pct'] = round(stats['correct'] / stats['total'] * 100, 1) if stats['total'] else 0
    for stats in topic_stats.values():
        stats['accuracy_pct'] = round(stats['correct'] / stats['total'] * 100, 1) if stats['total'] else 0

    attempt.is_completed = True
    attempt.submitted_at = timezone.now()
    attempt.correct_count = correct
    attempt.total_questions = total
    attempt.score_percentage = round(correct / total * 100, 2) if total else 0
    attempt.save(update_fields=[
        'is_completed', 'submitted_at',
        'correct_count', 'total_questions', 'score_percentage',
    ])

    from content.models import Subject
    subject_ids = {aq.question.subtopic.topic.subject_id for aq in items}
    subjects = Subject.objects.filter(id__in=subject_ids)
    recompute_user_progress(attempt.user, subjects)

    return {
        'total_questions': total,
        'answered': answered,
        'correct': correct,
        'incorrect': answered - correct,
        'unanswered': total - answered,
        'accuracy_pct': round(correct / total * 100, 1) if total else 0,
        'by_subject': subject_stats,
        'by_topic': topic_stats,
    }


def auto_finalize_if_expired(attempt):
    """
    If a timed attempt's clock has run out and it's still open,
    force-finalize it now. Call this at the top of any view that
    touches an in-progress attempt (answer, submit, review).

    NOTE: lazy expiry — only fires the next time an endpoint touches
    the attempt, not the instant expires_at passes. For true zero-touch
    expiry, add a scheduled sweep (Celery beat / cron command) later.
    """
    if (
        not attempt.is_completed
        and attempt.expires_at
        and timezone.now() > attempt.expires_at
    ):
        finalize_attempt(attempt)
        return True
    return False


def select_questions_for_sectional(subject, limit):
    """Pick N Qs from one subject. Random."""
    qs = Question.objects.filter(
        subtopic__topic__subject=subject,
        is_active=True, is_verified=True,
    ).order_by('?').values_list('id', flat=True)[:limit]

    question_ids = list(qs)
    if len(question_ids) < limit:
        raise QuizCreationError(
            f'{subject.name}: need {limit} Qs, only {len(question_ids)} verified in DB'
        )
    return question_ids


# MDCAT full-mock subject weightage. These five names must exactly
# match content.Subject.name in your DB.
FULL_MOCK_WEIGHTAGE = {
    'Biology': 0.34,
    'Chemistry': 0.27,
    'Physics': 0.27,
    'English': 0.09,
    'Logical Reasoning': 0.03,
}


def select_questions_for_full_mock(exam, total_questions=200):
    """
    Pick a full mock's questions respecting MDCAT subject weightage.
    Last subject absorbs the rounding remainder so counts sum exactly
    to total_questions.
    """
    from content.models import Subject

    subjects = Subject.objects.filter(exam=exam, is_active=True)
    subject_by_name = {s.name: s for s in subjects}

    question_ids = []
    allocated = 0
    names = list(FULL_MOCK_WEIGHTAGE.keys())

    for i, name in enumerate(names):
        subject = subject_by_name.get(name)
        if not subject:
            raise QuizCreationError(
                f'Full mock weightage expects subject "{name}" but exam has no such subject'
            )
        if i == len(names) - 1:
            count = total_questions - allocated
        else:
            count = round(total_questions * FULL_MOCK_WEIGHTAGE[name])
        question_ids.extend(select_questions_for_sectional(subject, count))
        allocated += count

    return question_ids


@transaction.atomic
def create_mock_attempt(user, mock_test, device_class='desktop', allow_breaks=True):
    """Create an Attempt from a MockTest template. Snapshots Qs, sets expires_at."""
    if not mock_test.is_active:
        raise QuizCreationError('Mock test is not active')

    if mock_test.kind == 'full':
        fixed = list(
            mock_test.questions.filter(is_active=True, is_verified=True)
            .order_by('paper_order', 'id')
            .values_list('id', flat=True)
        )
        if fixed:
            question_ids = fixed
        else:
            question_ids = select_questions_for_full_mock(mock_test.exam, mock_test.total_questions)
        mode = 'mock'
        subject = None
    elif mock_test.kind == 'sectional':
        if not mock_test.subject:
            raise QuizCreationError('Sectional mock must have a subject')
        question_ids = select_questions_for_sectional(
            mock_test.subject, mock_test.total_questions
        )
        mode = 'sectional'
        subject = mock_test.subject
    else:
        raise QuizCreationError(f'Unknown mock kind: {mock_test.kind}')

    now = timezone.now()
    from datetime import timedelta
    expires_at = now + timedelta(minutes=mock_test.duration_minutes)

    attempt = Attempt.objects.create(
        user=user,
        mode=mode,
        exam=mock_test.exam,
        subject=subject,
        mock_test=mock_test,
        total_questions=len(question_ids),
        expires_at=expires_at,
        allow_breaks=allow_breaks,
        device_class=device_class,
    )

    AttemptQuestion.objects.bulk_create([
        AttemptQuestion(
            attempt=attempt,
            question_id=qid,
            order_in_attempt=idx + 1,
        )
        for idx, qid in enumerate(question_ids)
    ])

    return attempt


def recompute_user_progress(user, subjects):
    """Refresh UserProgress rows for a user across the given subjects.

    Called from finalize_attempt after the score is cached. One upsert per
    subject that appeared in the attempt.
    """
    from content.models import Subtopic
    from .models import AttemptQuestion, UserProgress

    for subject in subjects:
        answered = AttemptQuestion.objects.filter(
            attempt__user=user,
            question__subtopic__topic__subject=subject,
            selected_option__isnull=False,
        ).exclude(selected_option='')

        questions_attempted = answered.count()
        correct = answered.filter(is_correct=True).count()
        accuracy = round(correct / questions_attempted * 100, 1) if questions_attempted else 0

        subtopics_attempted = answered.values('question__subtopic').distinct().count()

        subtopics_total = Subtopic.objects.filter(
            topic__subject=subject, is_active=True,
        ).count()

        coverage = round(subtopics_attempted / subtopics_total * 100, 1) if subtopics_total else 0

        UserProgress.objects.update_or_create(
            user=user,
            subject=subject,
            defaults={
                'coverage_pct': coverage,
                'subtopics_attempted': subtopics_attempted,
                'subtopics_total': subtopics_total,
                'questions_attempted': questions_attempted,
                'accuracy_pct': accuracy,
            },
        )

def get_weak_topics(user, exam, limit=5):
    """
    Return the user's weakest topics for an exam.

    Rules:
    - Require at least 5 completed sessions.
    - Analyze the latest 100 answered questions.
    - Ignore unanswered questions.
    - Require at least 3 answered questions per topic.
    - Lower accuracy = weaker topic.
    """

    completed_sessions = (
        Attempt.objects
        .filter(
            user=user,
            exam=exam,
            is_completed=True,
        )
        .count()
    )

    if completed_sessions < 5:
        return []

    recent_answers = (
        AttemptQuestion.objects
        .filter(
            attempt__user=user,
            attempt__exam=exam,
            attempt__is_completed=True,
            is_correct__isnull=False,
        )
        .select_related(
            "question__subtopic__topic",
        )
        .order_by(
            "-answered_at",
            "-id",
        )[:100]
    )

    topic_stats = {}

    for aq in recent_answers:
        topic = aq.question.subtopic.topic

        if topic.id not in topic_stats:
            topic_stats[topic.id] = {
                "topic_id": topic.id,
                "topic": topic.name,
                "attempted": 0,
                "correct": 0,
            }

        stats = topic_stats[topic.id]

        stats["attempted"] += 1

        if aq.is_correct:
            stats["correct"] += 1

    weak_topics = []

    for stats in topic_stats.values():

        if stats["attempted"] < 3:
            continue

        accuracy = round(
            stats["correct"] / stats["attempted"] * 100,
            1,
        )

        stats["accuracy_pct"] = accuracy

        weak_topics.append(stats)

    weak_topics.sort(
        key=lambda item: (
            item["accuracy_pct"],
            -item["attempted"],
        )
    )

    return weak_topics[:limit]        

def create_weak_topics_drill(user, exam, limit=20):
    """
    Create a practice attempt containing questions distributed
    across the user's weakest topics.

    Requires at least 5 completed sessions.
    """

    weak_topics = get_weak_topics(
        user=user,
        exam=exam,
        limit=5,
    )

    if not weak_topics:
        raise QuizCreationError(
            "You need at least 5 completed sessions and enough "
            "answered questions to generate a weak-topic drill."
        )

    topic_ids = [
        topic["topic_id"]
        for topic in weak_topics
    ]

    # Prefer questions the student has not answered before.
    answered_question_ids = (
        AttemptQuestion.objects
        .filter(
            attempt__user=user,
            attempt__exam=exam,
            selected_option__isnull=False,
        )
        .values_list("question_id", flat=True)
    )

    # Fair starting allocation across weak topics.
    topic_count = len(topic_ids)
    base = limit // topic_count
    remainder = limit % topic_count

    allocations = {}

    for index, topic_id in enumerate(topic_ids):
        allocations[topic_id] = base + (
            1 if index < remainder else 0
        )

    selected_questions = []
    selected_ids = set()
    remaining_slots = 0

    # First pass: unseen questions.
    for topic_id in topic_ids:
        target = allocations[topic_id]

        pool = (
            Question.objects
            .filter(
                is_active=True,
                is_verified=True,
                subtopic__topic_id=topic_id,
                subtopic__topic__subject__exam=exam,
            )
            .exclude(
                id__in=answered_question_ids,
            )
            .order_by("?")
        )

        topic_questions = list(pool[:target])

        selected_questions.extend(topic_questions)

        selected_ids.update(
            question.id
            for question in topic_questions
        )

        remaining_slots += target - len(topic_questions)

    # Second pass: redistribute missing slots across weak topics.
    if remaining_slots > 0:
        fallback_pool = (
            Question.objects
            .filter(
                is_active=True,
                is_verified=True,
                subtopic__topic_id__in=topic_ids,
                subtopic__topic__subject__exam=exam,
            )
            .exclude(
                id__in=selected_ids,
            )
            .order_by("?")
        )

        fallback_questions = list(
            fallback_pool[:remaining_slots]
        )

        selected_questions.extend(fallback_questions)

        selected_ids.update(
            question.id
            for question in fallback_questions
        )

    if len(selected_questions) < limit:
        raise QuizCreationError(
            f"Not enough questions available for a "
            f"{limit}-question weak-topic drill."
        )

    selected_questions = selected_questions[:limit]

    attempt = Attempt.objects.create(
        user=user,
        exam=exam,
        mode="practice",
        total_questions=len(selected_questions),
    )

    AttemptQuestion.objects.bulk_create([
        AttemptQuestion(
            attempt=attempt,
            question=question,
            order_in_attempt=index,
        )
        for index, question in enumerate(
            selected_questions,
            start=1,
        )
    ])

    return attempt

@transaction.atomic
def create_past_paper_attempt(user, past_paper, device_class='desktop'):
    """Create an Attempt from a PastPaper. Snapshots all active + verified Qs
    in the paper, in their original order (Question.id).

    No timer — students take past papers at their own pace, revisitable.
    """
    from content.models import PastPaper as _PP  # avoid circular

    if not past_paper.is_active:
        raise QuizCreationError('Past paper is not active')

    question_ids = list(
        Question.objects
        .filter(past_paper=past_paper, is_active=True, is_verified=True)
        .order_by('id')
        .values_list('id', flat=True)
    )

    if not question_ids:
        raise QuizCreationError('No verified questions found in this paper')

    attempt = Attempt.objects.create(
        user=user,
        mode='past_paper',
        exam=past_paper.exam,
        past_paper=past_paper,
        total_questions=len(question_ids),
        device_class=device_class,
    )

    AttemptQuestion.objects.bulk_create([
        AttemptQuestion(
            attempt=attempt,
            question_id=qid,
            order_in_attempt=idx + 1,
        )
        for idx, qid in enumerate(question_ids)
    ])

    return attempt