from datetime import timedelta

from django.conf import settings
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.models import is_guest
from content.models import Question, Exam, Subject, Topic, Subtopic
from payments.models import has_active_subscription

from .models import (
    Attempt,
    AttemptQuestion,
    AttemptViolation,
    MockTest,
    UserProgress,
)

from .services import (
    create_practice_attempt,
    finalize_attempt,
    QuizCreationError,
    get_weak_topics,
    create_weak_topics_drill,
)

from .serializers import (
    QuestionListSerializer,
    AttemptCreateSerializer,
    AttemptDetailSerializer,
    AnswerSubmitSerializer,
    MockTestSerializer,
)

class QuestionListView(generics.ListAPIView):
    """GET /api/questions/?exam=1&subject=2&topic=5&difficulty=medium"""
    serializer_class = QuestionListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Question.objects.filter(is_active=True, is_verified=True)
        params = self.request.query_params

        if exam_id := params.get('exam'):
            qs = qs.filter(subtopic__topic__subject__exam_id=exam_id)
        if subject_id := params.get('subject'):
            qs = qs.filter(subtopic__topic__subject_id=subject_id)
        if topic_id := params.get('topic'):
            qs = qs.filter(subtopic__topic_id=topic_id)
        if difficulty := params.get('difficulty'):
            qs = qs.filter(difficulty=difficulty)

        return qs.select_related('subtopic__topic__subject').order_by('id')


class AttemptCreateView(APIView):
    """POST /api/attempts/ — start a practice session."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AttemptCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        exam = get_object_or_404(Exam, id=data['exam_id'])
        subject = Subject.objects.filter(id=data.get('subject_id')).first() if data.get('subject_id') else None
        topic = Topic.objects.filter(id=data.get('topic_id')).first() if data.get('topic_id') else None
        subtopic = Subtopic.objects.filter(id=data.get('subtopic_id')).first() if data.get('subtopic_id') else None

        try:
            attempt = create_practice_attempt(
                user=request.user,
                exam=exam,
                subject=subject,
                topic=topic,
                subtopic=subtopic,
                difficulty=data.get('difficulty'),
                limit=data.get('limit', 20),
            )
        except QuizCreationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            AttemptDetailSerializer(attempt, context={'request': request}).data,
            status=status.HTTP_201_CREATED,
        )


class AttemptAnswerView(APIView):
    """POST /api/attempts/<attempt_id>/answer/ — record an answer."""
    permission_classes = [IsAuthenticated]

    def post(self, request, attempt_id):
        attempt = get_object_or_404(Attempt, id=attempt_id, user=request.user)

        if attempt.is_completed:
            return Response(
                {'error': 'Attempt already submitted'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Mock expiry check (harmless for practice — expires_at is null)
        if attempt.expires_at and timezone.now() > attempt.expires_at:
            return Response(
                {'error': 'Attempt time expired'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = AnswerSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        aq = get_object_or_404(
            AttemptQuestion,
            id=data['attempt_question_id'],
            attempt=attempt,
        )

        # Normalize case: AttemptQuestion stores lowercase (a/b/c/d),
        # Question.correct_answer stores uppercase (A/B/C/D).
        selected_upper = data['selected_option'].upper()
        aq.selected_option = data['selected_option']
        aq.is_correct = (selected_upper == aq.question.correct_answer)
        aq.time_spent_seconds = data['time_spent_seconds']
        aq.answered_at = timezone.now()
        aq.save()

        # For practice mode — return correctness immediately (feedback per Q)
        # For mocks later — we'll gate this behind mode=='practice'
        return Response({
            'is_correct': aq.is_correct,
            'correct_answer': aq.question.correct_answer if attempt.mode == 'practice' else None,
        })


class AttemptSubmitView(APIView):
    """POST /api/quiz/attempts/<id>/submit/ — finalize and score."""
    permission_classes = [IsAuthenticated]

    def post(self, request, attempt_id):
        attempt = get_object_or_404(Attempt, id=attempt_id, user=request.user)

        try:
            breakdown = finalize_attempt(attempt)
        except QuizCreationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'attempt_id': attempt.id,
            'submitted_at': attempt.submitted_at,
            **breakdown,
        })


class AttemptReviewView(APIView):
    """GET /api/quiz/attempts/<id>/ — review mode. Only after submit."""
    permission_classes = [IsAuthenticated]

    def get(self, request, attempt_id):
        attempt = get_object_or_404(Attempt, id=attempt_id, user=request.user)

        if not attempt.is_completed:
            return Response(
                {'error': 'Attempt not yet submitted. Submit first to review.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        items = attempt.items.select_related(
            'question__subtopic__topic__subject'
        ).order_by('order_in_attempt')

        review_items = [{
            'order': aq.order_in_attempt,
            'question_id': aq.question.id,
            'question_text': aq.question.question_text,
            'option_a': aq.question.option_a,
            'option_b': aq.question.option_b,
            'option_c': aq.question.option_c,
            'option_d': aq.question.option_d,
            'selected_option': aq.selected_option,
            'correct_answer': aq.question.correct_answer,
            'is_correct': aq.is_correct,
            'time_spent_seconds': aq.time_spent_seconds,
            'subject': aq.question.subtopic.topic.subject.name,
            'topic': aq.question.subtopic.topic.name,
        } for aq in items]

        return Response({
            'attempt_id': attempt.id,
            'mode': attempt.mode,
            'submitted_at': attempt.submitted_at,
            'score_correct': attempt.correct_count,
            'score_total': attempt.total_questions,
            'score_percentage': str(attempt.score_percentage),
            'items': review_items,
        })

class AnalyticsDashboardView(APIView):
    """
    GET /api/quiz/analytics/

    Returns a compact dashboard summary for the authenticated student.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        completed_attempts = (
            Attempt.objects
            .filter(
                user=user,
                is_completed=True,
            )
            .order_by("-submitted_at")
        )

        total_attempts = completed_attempts.count()

        total_questions_attempted = sum(
            attempt.total_questions
            for attempt in completed_attempts
        )

        total_correct = sum(
            attempt.correct_count
            for attempt in completed_attempts
        )

        overall_accuracy = (
            round(
                total_correct / total_questions_attempted * 100,
                2,
            )
            if total_questions_attempted
            else 0
        )

        progress_rows = (
            UserProgress.objects
            .filter(user=user)
            .select_related("subject")
            .order_by("subject__order", "subject__name")
        )

        subjects = [
            {
                "subject_id": progress.subject_id,
                "subject": progress.subject.name,
                "coverage_pct": float(progress.coverage_pct),
                "questions_attempted": progress.questions_attempted,
                "accuracy_pct": float(progress.accuracy_pct),
            }
            for progress in progress_rows
        ]

        recent_attempts = [
            {
                "id": attempt.id,
                "mode": attempt.mode,
                "total_questions": attempt.total_questions,
                "correct_count": attempt.correct_count,
                "score_percentage": str(
                    attempt.score_percentage
                ),
                "submitted_at": attempt.submitted_at,
            }
            for attempt in completed_attempts[:5]
        ]

        # Streak: consecutive calendar days (server timezone) with
        # at least one completed attempt, ending today or yesterday.
        # (Yesterday still counts so the streak doesn't reset to 0
        # the moment the clock rolls over before today's first attempt.)
        distinct_days = sorted(
            {
                timezone.localtime(attempt.submitted_at).date()
                for attempt in completed_attempts
                if attempt.submitted_at
            },
            reverse=True,
        )

        current_streak = 0

        if distinct_days:
            today = timezone.localdate()

            if distinct_days[0] in (today, today - timedelta(days=1)):
                current_streak = 1
                expected = distinct_days[0] - timedelta(days=1)

                for day in distinct_days[1:]:
                    if day == expected:
                        current_streak += 1
                        expected -= timedelta(days=1)
                    else:
                        break

        return Response({
            "overview": {
                "total_attempts": total_attempts,
                "question_attempts": total_questions_attempted,
                "correct_answers": total_correct,
                "overall_accuracy": overall_accuracy,
                "current_streak": current_streak,
            },
            "subjects": subjects,
            "recent_attempts": recent_attempts,
        })

class WeakTopicsView(APIView):
    """
    GET /api/quiz/weak-topics/?exam=1

    Returns the student's weakest topics for the selected exam.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        exam_id = request.query_params.get("exam")

        if not exam_id:
            return Response(
                {"error": "exam query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        exam = get_object_or_404(
            Exam,
            id=exam_id,
            is_active=True,
        )

        weak_topics = get_weak_topics(
            user=request.user,
            exam=exam,
            limit=5,
        )

        return Response({
            "exam": {
                "id": exam.id,
                "name": exam.name,
                "slug": exam.slug,
            },
            "eligible": (
                Attempt.objects.filter(
                    user=request.user,
                    exam=exam,
                    is_completed=True,
                ).count() >= 5
            ),
            "weak_topics": weak_topics,
        })    
    
class MockTestListView(generics.ListAPIView):
    """GET /api/quiz/mocks/?exam=1 — browsable list of mock test templates.

    Full mocks and sectional mocks both come back here; the frontend
    splits them by `kind`. Feeds the Mock tab AND the public per-exam
    landing page (/exams/[slug]) — public/read-only like the past-paper
    and syllabus browse endpoints in content/views.py, so visitors can see
    what's inside an exam before signing up.
    """
    serializer_class = MockTestSerializer
    permission_classes = [AllowAny]
    pagination_class = None

    def get_queryset(self):
        qs = MockTest.objects.filter(is_active=True).select_related('subject')

        if exam_id := self.request.query_params.get('exam'):
            qs = qs.filter(exam_id=exam_id)

        return qs

class MockStartView(APIView):
    """POST /api/quiz/mocks/<mock_id>/start/ — begin a mock attempt from a template.

    Body: {"allow_breaks": true|false, "device_class": "desktop|mobile|tablet"}
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, mock_id):
        from .models import MockTest
        from .services import create_mock_attempt

        mock_test = get_object_or_404(MockTest, id=mock_id, is_active=True)

        if not mock_test.is_free:
            if is_guest(request.user):
                return Response(
                    {'error': 'signup_required', 'message': 'Sign up to start this mock.'},
                    status=status.HTTP_403_FORBIDDEN,
                )
            # FREE_LAUNCH_MODE: signed-up users still need an account (above),
            # but the subscription check itself is bypassed — see settings.py.
            if not settings.FREE_LAUNCH_MODE and not has_active_subscription(request.user, mock_test.exam):
                return Response(
                    {'error': 'subscription_required', 'message': 'Upgrade your plan to start this mock.'},
                    status=status.HTTP_403_FORBIDDEN,
                )

        allow_breaks = request.data.get('allow_breaks', True)
        device_class = request.data.get('device_class', 'desktop')

        try:
            attempt = create_mock_attempt(
                user=request.user,
                mock_test=mock_test,
                device_class=device_class,
                allow_breaks=allow_breaks,
            )
        except QuizCreationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            AttemptDetailSerializer(attempt, context={'request': request}).data,
            status=status.HTTP_201_CREATED,
        )

class AttemptViolationView(APIView):
    """
    POST /api/quiz/attempts/<attempt_id>/violation/

    Body:
    {
        "violation_type": "tab_hidden"
    }

    Rules:
    1st violation -> record only
    2nd violation -> warning + alarm
    3rd violation -> terminate mock + finalize result
    """

    permission_classes = [IsAuthenticated]

    ALLOWED_TYPES = {
        "tab_hidden",
        "window_blur",
        "fullscreen_exit",
        "copy_attempt",
    }

    def post(self, request, attempt_id):
        attempt = get_object_or_404(
            Attempt,
            id=attempt_id,
            user=request.user,
        )

        if attempt.mode not in ("mock", "sectional"):
            return Response(
                {"error": "Integrity violations only apply to mock attempts."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if attempt.is_completed:
            return Response(
                {"error": "Attempt already completed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        violation_type = request.data.get("violation_type")

        if violation_type not in self.ALLOWED_TYPES:
            return Response(
                {
                    "error": (
                        "Invalid violation_type. "
                        "Use tab_hidden, window_blur, fullscreen_exit, or copy_attempt."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        violation = AttemptViolation.objects.create(
            attempt=attempt,
            violation_type=violation_type,
        )

        violation_count = attempt.violations.count()

        # 1st violation
        if violation_count == 1:
            return Response({
                "attempt_id": attempt.id,
                "violation_id": violation.id,
                "violation_count": violation_count,
                "action": "record",
                "message": "First integrity violation recorded.",
                "alarm": False,
                "terminate": False,
            })

        # 2nd violation
        if violation_count == 2:
            attempt.integrity_flagged = True
            attempt.save(update_fields=["integrity_flagged"])

            return Response({
                "attempt_id": attempt.id,
                "violation_id": violation.id,
                "violation_count": violation_count,
                "action": "warn",
                "message": "Second integrity violation. One more violation will end the mock.",
                "alarm": True,
                "terminate": False,
            })

        # 3rd violation or later
        attempt.integrity_flagged = True
        attempt.save(update_fields=["integrity_flagged"])

        try:
            breakdown = finalize_attempt(attempt)
        except QuizCreationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({
            "attempt_id": attempt.id,
            "violation_id": violation.id,
            "violation_count": violation_count,
            "action": "terminate",
            "message": "Mock terminated due to repeated integrity violations.",
            "alarm": True,
            "terminate": True,
            "result": breakdown,
        })    

class WeakTopicsDrillView(APIView):
    """
    POST /api/quiz/weak-topics/drill/?exam=1

    Creates a 20-question practice attempt from weak topics.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        exam_id = request.query_params.get("exam")

        if not exam_id:
            return Response(
                {"error": "exam query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        exam = get_object_or_404(
            Exam,
            id=exam_id,
            is_active=True,
        )

        try:
            attempt = create_weak_topics_drill(
                user=request.user,
                exam=exam,
                limit=20,
            )
        except QuizCreationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            AttemptDetailSerializer(attempt, context={'request': request}).data,
            status=status.HTTP_201_CREATED,
        )

class MockPerformanceReportView(APIView):
    """
    GET /api/quiz/mocks/report/

    Returns a simple performance report for the latest completed mock.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempt = (
            Attempt.objects
            .filter(
                user=request.user,
                mode="mock",
                is_completed=True,
            )
            .order_by("-submitted_at")
            .first()
        )

        if not attempt:
            return Response({
                "available": False,
                "message": "No completed mock test found.",
            })

        items = (
            attempt.items
            .filter(is_correct__isnull=False)
            .select_related(
                "question__subtopic__topic__subject",
            )
        )

        answered_count = items.count()

        unanswered_count = (
            attempt.items
            .filter(is_correct__isnull=True)
            .count()
        )

        subject_stats = {}
        topic_stats = {}

        for aq in items:
            subject = aq.question.subtopic.topic.subject
            topic = aq.question.subtopic.topic

            subject_data = subject_stats.setdefault(
                subject.id,
                {
                    "subject_id": subject.id,
                    "subject": subject.name,
                    "attempted": 0,
                    "correct": 0,
                },
            )

            subject_data["attempted"] += 1

            if aq.is_correct:
                subject_data["correct"] += 1

            topic_data = topic_stats.setdefault(
                topic.id,
                {
                    "topic_id": topic.id,
                    "topic": topic.name,
                    "subject": subject.name,
                    "attempted": 0,
                    "correct": 0,
                },
            )

            topic_data["attempted"] += 1

            if aq.is_correct:
                topic_data["correct"] += 1

        subjects = []

        for data in subject_stats.values():
            data["accuracy_pct"] = round(
                data["correct"] / data["attempted"] * 100,
                1,
            )
            subjects.append(data)

        topics = []

        for data in topic_stats.values():
            data["accuracy_pct"] = round(
                data["correct"] / data["attempted"] * 100,
                1,
            )
            topics.append(data)

        subjects.sort(
            key=lambda item: item["accuracy_pct"],
            reverse=True,
        )

        topics.sort(
            key=lambda item: item["accuracy_pct"],
        )

        strengths = [
            item
            for item in subjects
            if item["accuracy_pct"] >= 70
        ]

        weaknesses = [
            item
            for item in subjects
            if item["accuracy_pct"] < 60
        ]

        focus_topics = [
            {
                "topic_id": item["topic_id"],
                "topic": item["topic"],
                "subject": item["subject"],
                "accuracy_pct": item["accuracy_pct"],
            }
            for item in topics[:5]
        ]

        return Response({
            "available": True,
            "mock": {
                "attempt_id": attempt.id,
                "submitted_at": attempt.submitted_at,
                "total_questions": attempt.total_questions,
                "answered_count": answered_count,
                "unanswered_count": unanswered_count,
                "correct_count": attempt.correct_count,
                "score_percentage": str(
                    attempt.score_percentage
                ),
            },
            "strengths": strengths,
            "weaknesses": weaknesses,
            "subjects": subjects,
            "topics": topics,
            "two_week_focus": focus_topics,
        })

class MockFocusPlanView(APIView):
    """
    GET /api/quiz/mocks/focus-plan/

    Returns a simple 14-day focus plan based on the
    latest completed mock's weakest topics.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        attempt = (
            Attempt.objects
            .filter(
                user=request.user,
                mode="mock",
                is_completed=True,
            )
            .order_by("-submitted_at")
            .first()
        )

        if not attempt:
            return Response({
                "available": False,
                "message": "Complete a mock test first.",
            })

        items = (
            attempt.items
            .filter(is_correct__isnull=False)
            .select_related(
                "question__subtopic__topic__subject",
            )
        )

        topic_stats = {}

        for aq in items:
            topic = aq.question.subtopic.topic
            subject = topic.subject

            data = topic_stats.setdefault(
                topic.id,
                {
                    "topic_id": topic.id,
                    "topic": topic.name,
                    "subject_id": subject.id,
                    "subject": subject.name,
                    "attempted": 0,
                    "correct": 0,
                },
            )

            data["attempted"] += 1

            if aq.is_correct:
                data["correct"] += 1

        topics = []

        for data in topic_stats.values():
            data["accuracy_pct"] = round(
                data["correct"] / data["attempted"] * 100,
                1,
            )
            topics.append(data)

        topics.sort(
            key=lambda item: item["accuracy_pct"]
        )

        # Keep only topics with actual answered questions.
        focus_topics = topics[:5]

        if not focus_topics:
            return Response({
                "available": True,
                "message": "This mock has no answered questions.",
                "days": [],
            })

        # Divide the 14 days across up to 5 topics.
        topic_count = len(focus_topics)
        base_days = 14 // topic_count
        extra_days = 14 % topic_count

        days = []
        current_day = 1

        for index, topic in enumerate(focus_topics):
            days_for_topic = base_days + (
                1 if index < extra_days else 0
            )

            for offset in range(days_for_topic):
                days.append({
                    "day": current_day + offset,
                    "topic_id": topic["topic_id"],
                    "topic": topic["topic"],
                    "subject_id": topic["subject_id"],
                    "subject": topic["subject"],
                    "activity": (
                        f"Drill {topic['topic']} until you can solve it "
                        f"without hesitation — currently {topic['accuracy_pct']}% accuracy."
                    ),
                    "accuracy_pct": topic["accuracy_pct"],
                })

            current_day += days_for_topic

        return Response({
            "available": True,
            "mock_attempt_id": attempt.id,
            "duration_days": 14,
            "focus_topics": focus_topics,
            "days": days,
        })

class TestDatePlanView(APIView):
    """
    GET /api/quiz/study-plan/

    A syllabus-coverage pacing plan built from the student's target_date —
    "cover the whole syllabus, subject by subject, before test day."

    Distinct from MockFocusPlanView above: that one drills WEAK topics
    after a mock; this one paces the FULL syllabus against a real deadline,
    independent of whether any mock has been taken yet.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = getattr(request.user, 'profile', None)

        if profile is None:
            return Response({
                "available": False,
                "message": "Complete your profile (pick your exam) in Settings to unlock a pacing plan.",
            })

        if not profile.target_date:
            return Response({
                "available": False,
                "message": "Set your test date in Settings to unlock a pacing plan.",
            })

        today = timezone.localdate()
        days_remaining = (profile.target_date - today).days

        if days_remaining <= 0:
            return Response({
                "available": True,
                "target_date": profile.target_date,
                "days_remaining": days_remaining,
                "weeks_remaining": 0,
                "message": "Your test date has passed — update it in Settings if it changed.",
                "weeks": [],
                "skipped_subjects": [],
            })

        topic_qs = Topic.objects.filter(is_active=True).order_by("order", "name")

        all_subjects = list(
            Subject.objects.filter(exam=profile.primary_exam, is_active=True)
            .prefetch_related(Prefetch("topics", queryset=topic_qs))
            .order_by("-weight_percent", "order", "name")
        )

        if not all_subjects:
            return Response({
                "available": True,
                "target_date": profile.target_date,
                "days_remaining": days_remaining,
                "weeks_remaining": max(1, days_remaining // 7),
                "message": "No syllabus is set up for your exam yet.",
                "weeks": [],
                "skipped_subjects": [],
            })

        weeks_remaining = max(1, days_remaining // 7)
        skipped_subjects = []

        if weeks_remaining < len(all_subjects):
            # Not enough weeks left for every subject to get its own —
            # prioritize by exam weight, one week each, and say so.
            subjects = all_subjects[:weeks_remaining]
            skipped_subjects = [s.name for s in all_subjects[weeks_remaining:]]
            weeks_per_subject = [1] * len(subjects)
        else:
            subjects = all_subjects
            total_weight = sum(s.weight_percent for s in subjects) or len(subjects)
            weeks_per_subject = [
                max(1, round(s.weight_percent / total_weight * weeks_remaining))
                for s in subjects
            ]
            # Nudge the split so it sums to exactly weeks_remaining.
            while sum(weeks_per_subject) > weeks_remaining:
                i = weeks_per_subject.index(max(weeks_per_subject))
                weeks_per_subject[i] -= 1
            while sum(weeks_per_subject) < weeks_remaining:
                i = weeks_per_subject.index(min(weeks_per_subject))
                weeks_per_subject[i] += 1

        weeks = []
        week_cursor = 1

        for subject, subject_weeks in zip(subjects, weeks_per_subject):
            topics = list(subject.topics.all())
            base = len(topics) // subject_weeks
            extra = len(topics) % subject_weeks
            cursor = 0

            for w in range(subject_weeks):
                count = base + (1 if w < extra else 0)
                chunk = topics[cursor:cursor + count]
                cursor += count

                start_date = today + timedelta(days=(week_cursor - 1) * 7)

                weeks.append({
                    "week": week_cursor,
                    "start_date": start_date,
                    "end_date": start_date + timedelta(days=6),
                    "subject_id": subject.id,
                    "subject": subject.name,
                    "topics": [{"id": t.id, "name": t.name} for t in chunk],
                })
                week_cursor += 1

        return Response({
            "available": True,
            "target_date": profile.target_date,
            "days_remaining": days_remaining,
            "weeks_remaining": weeks_remaining,
            "weeks": weeks,
            "skipped_subjects": skipped_subjects,
        })

class PastPaperStartView(APIView):
    """POST /api/quiz/past-papers/<paper_id>/start/ — begin (or resume) a past paper.

    If the user already has an incomplete attempt on this paper, returns THAT
    attempt instead of creating a new one. Enables the "Continue where you
    left off" UX.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, paper_id):
        from content.models import PastPaper
        from .services import create_past_paper_attempt

        paper = get_object_or_404(PastPaper, id=paper_id, is_active=True)

        if not paper.is_free:
            if is_guest(request.user):
                return Response(
                    {'error': 'signup_required', 'message': 'Sign up to start this paper.'},
                    status=status.HTTP_403_FORBIDDEN,
                )
            # FREE_LAUNCH_MODE: signed-up users still need an account (above),
            # but the subscription check itself is bypassed — see settings.py.
            if not settings.FREE_LAUNCH_MODE and not has_active_subscription(request.user, paper.exam):
                return Response(
                    {'error': 'subscription_required', 'message': 'Upgrade your plan to start this paper.'},
                    status=status.HTTP_403_FORBIDDEN,
                )

        # Resume in-progress attempt if one exists
        existing = Attempt.objects.filter(
            user=request.user,
            past_paper=paper,
            is_completed=False,
        ).order_by('-started_at').first()

        if existing:
            return Response(
                AttemptDetailSerializer(existing, context={'request': request}).data,
                status=status.HTTP_200_OK,
            )

        try:
            attempt = create_past_paper_attempt(
                user=request.user,
                past_paper=paper,
                device_class=request.data.get('device_class', 'desktop'),
            )
        except QuizCreationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            AttemptDetailSerializer(attempt, context={'request': request}).data,
            status=status.HTTP_201_CREATED,
        )