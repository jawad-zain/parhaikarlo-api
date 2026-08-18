from django.urls import path
from .views import ExamListView, PastPaperListView, SyllabusView, TopicNoteView

urlpatterns = [
    path('exams/', ExamListView.as_view(), name='exam-list'),
    path('past-papers/', PastPaperListView.as_view(), name='past-paper-list'),
    path('syllabus/', SyllabusView.as_view(), name='syllabus'),
    path('topics/<int:topic_id>/note/', TopicNoteView.as_view(), name='topic-note'),
]