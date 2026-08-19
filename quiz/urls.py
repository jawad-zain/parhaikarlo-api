from django.urls import path

from .views import (
    PastPaperStartView,
    QuestionListView,
    AnalyticsDashboardView,
    WeakTopicsView,
    AttemptCreateView,
    AttemptAnswerView,
    AttemptSubmitView,
    AttemptReviewView,
    MockStartView,
    AttemptViolationView,
    WeakTopicsDrillView,
    MockPerformanceReportView,
    MockFocusPlanView,
    TestDatePlanView,
    MockTestListView,
)


urlpatterns = [
    path(
        'questions/',
        QuestionListView.as_view(),
        name='question-list',
    ),

    path(
    "mocks/",
    MockTestListView.as_view(),
    name="mock-list",
    ),

    path(
    "mocks/focus-plan/",
    MockFocusPlanView.as_view(),
    name="mock-focus-plan",
    ),

    path(
    "study-plan/",
    TestDatePlanView.as_view(),
    name="study-plan",
    ),

    path(
    "mocks/report/",
    MockPerformanceReportView.as_view(),
    name="mock-performance-report",
    ),

    path(
    'analytics/',
    AnalyticsDashboardView.as_view(),
    name='analytics-dashboard',
    ),

    path(
    "weak-topics/",
    WeakTopicsView.as_view(),
    name="weak-topics",
    ),

    path(
        'attempts/',
        AttemptCreateView.as_view(),
        name='attempt-create',
    ),

    path(
        'attempts/<int:attempt_id>/',
        AttemptReviewView.as_view(),
        name='attempt-review',
    ),

    path(
        'attempts/<int:attempt_id>/answer/',
        AttemptAnswerView.as_view(),
        name='attempt-answer',
    ),

    path(
        'attempts/<int:attempt_id>/submit/',
        AttemptSubmitView.as_view(),
        name='attempt-submit',
    ),

    path(
        'attempts/<int:attempt_id>/violation/',
        AttemptViolationView.as_view(),
        name='attempt-violation',
    ),

    path(
        'mocks/<int:mock_id>/start/',
        MockStartView.as_view(),
        name='mock-start',
    ),

    path(
    "weak-topics/drill/",
    WeakTopicsDrillView.as_view(),
    name="weak-topics-drill",
    ),

    path(
        'past-papers/<int:paper_id>/start/',
        PastPaperStartView.as_view(),
        name='past-paper-start',
    ),

] 