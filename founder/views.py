from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count, Q
from django.shortcuts import render

from content.models import Question, PastPaper, Subject, Subtopic
from .models import BuildTask


def is_superuser(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_superuser)
def founder_dashboard(request):
    # Overall Q stats
    total_qs = Question.objects.count()
    active_qs = Question.objects.filter(is_active=True).count()
    verified_qs = Question.objects.filter(is_active=True, is_verified=True).count()
    needs_review = Question.objects.filter(is_active=True, is_verified=False).count()
    verified_pct = round(verified_qs / active_qs * 100, 1) if active_qs else 0

    # Per-paper counts
    papers = PastPaper.objects.annotate(
        q_count=Count('questions', filter=Q(questions__is_active=True)),
        verified_count=Count('questions', filter=Q(questions__is_active=True, questions__is_verified=True)),
    ).order_by('-year')

    # Per-subject verified counts
    subjects = Subject.objects.annotate(
        q_count=Count('topics__subtopics__questions', filter=Q(topics__subtopics__questions__is_active=True)),
        verified_count=Count(
            'topics__subtopics__questions',
            filter=Q(topics__subtopics__questions__is_active=True, topics__subtopics__questions__is_verified=True),
        ),
    ).order_by('-q_count')

    # Coverage gaps — subtopics with zero active Qs
    empty_subtopics = Subtopic.objects.annotate(
        q_count=Count('questions', filter=Q(questions__is_active=True)),
    ).filter(q_count=0, is_active=True).select_related('topic__subject').order_by(
        'topic__subject__name', 'topic__name', 'name',
    )

    # Build checklist grouped by week
    tasks = BuildTask.objects.all()
    tasks_by_week = {}
    for t in tasks:
        tasks_by_week.setdefault(t.week, []).append(t)
    weeks_sorted = sorted(tasks_by_week.items())

    total_tasks = tasks.count()
    done_tasks = tasks.filter(is_done=True).count()
    tasks_pct = round(done_tasks / total_tasks * 100, 1) if total_tasks else 0

    context = {
        'total_qs': total_qs,
        'active_qs': active_qs,
        'verified_qs': verified_qs,
        'needs_review': needs_review,
        'verified_pct': verified_pct,
        'papers': papers,
        'subjects': subjects,
        'empty_subtopics': empty_subtopics,
        'empty_subtopics_count': empty_subtopics.count(),
        'weeks_sorted': weeks_sorted,
        'done_tasks': done_tasks,
        'total_tasks': total_tasks,
        'tasks_pct': tasks_pct,
    }
    return render(request, 'founder/dashboard.html', context)