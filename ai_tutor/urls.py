from django.urls import path
from .views import (
    QuestionExplainView,
    QuestionExplanationReportView,
)


urlpatterns = [
    path(
        "questions/<int:question_id>/explain/",
        QuestionExplainView.as_view(),
        name="question-explain",
    ),
    path(
        "questions/<int:question_id>/explain/report/",
        QuestionExplanationReportView.as_view(),
        name="question-explanation-report",
    ),
]