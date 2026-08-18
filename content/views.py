from django.db.models import Count, Prefetch, Q
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ConceptNote, Exam, PastPaper, Subject, Topic, Subtopic
from .serializers import ExamSerializer, PastPaperSerializer


class ExamListView(generics.ListAPIView):
    """GET /api/content/exams/ — list all active exams."""
    serializer_class = ExamSerializer
    permission_classes = [AllowAny]  # public — needed for signup screen

    def get_queryset(self):
        return Exam.objects.filter(is_active=True).order_by('name')


class PastPaperListView(generics.ListAPIView):
    """GET /api/content/past-papers/?exam=1

    Returns papers with counts baked in — one DB query, no N+1.
    Public so the Past Papers page renders even before login.
    """
    serializer_class = PastPaperSerializer
    permission_classes = [AllowAny]
    pagination_class = None  # small list, don't paginate

    def get_queryset(self):
        qs = PastPaper.objects.filter(is_active=True).annotate(
            question_count=Count('questions', filter=Q(questions__is_active=True)),
            verified_count=Count(
                'questions',
                filter=Q(questions__is_active=True, questions__is_verified=True),
            ),
            easy_count=Count(
                'questions',
                filter=Q(questions__is_active=True, questions__difficulty='easy'),
            ),
            medium_count=Count(
                'questions',
                filter=Q(questions__is_active=True, questions__difficulty='medium'),
            ),
            hard_count=Count(
                'questions',
                filter=Q(questions__is_active=True, questions__difficulty='hard'),
            ),
        ).order_by('-year')

        if exam_id := self.request.query_params.get('exam'):
            qs = qs.filter(exam_id=exam_id)

        return qs


class SyllabusView(APIView):
    """
    GET /api/content/syllabus/?exam=1

    Returns the full subject -> topic -> subtopic tree for an exam,
    with question counts and concept-note availability baked in.
    Powers the Syllabus tab.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        exam_id = request.query_params.get('exam')

        if not exam_id:
            return Response(
                {'error': 'exam query parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        exam = get_object_or_404(Exam, id=exam_id, is_active=True)

        subtopic_qs = (
            Subtopic.objects.filter(is_active=True)
            .annotate(question_count=Count('questions', filter=Q(questions__is_active=True)))
            .order_by('order', 'name')
        )

        topic_qs = (
            Topic.objects.filter(is_active=True)
            .select_related('concept_note')
            .prefetch_related(Prefetch('subtopics', queryset=subtopic_qs))
            .order_by('order', 'name')
        )

        subjects = (
            Subject.objects.filter(exam=exam, is_active=True)
            .prefetch_related(Prefetch('topics', queryset=topic_qs))
            .order_by('order', 'name')
        )

        payload = []

        for subject in subjects:
            topics = []

            for topic in subject.topics.all():
                subtopics = [
                    {
                        'id': st.id,
                        'name': st.name,
                        'slug': st.slug,
                        'question_count': st.question_count,
                    }
                    for st in topic.subtopics.all()
                ]

                try:
                    has_note = topic.concept_note.is_active
                except ConceptNote.DoesNotExist:
                    has_note = False

                topics.append({
                    'id': topic.id,
                    'name': topic.name,
                    'slug': topic.slug,
                    'question_count': sum(s['question_count'] for s in subtopics),
                    'has_note': has_note,
                    'subtopics': subtopics,
                })

            payload.append({
                'id': subject.id,
                'name': subject.name,
                'slug': subject.slug,
                'weight_percent': subject.weight_percent,
                'topics': topics,
            })

        return Response({
            'exam': {'id': exam.id, 'name': exam.name, 'slug': exam.slug},
            'subjects': payload,
        })


class TopicNoteView(APIView):
    """GET /api/content/topics/<topic_id>/note/ — full concept note for a topic."""
    permission_classes = [AllowAny]

    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id, is_active=True)

        try:
            note = topic.concept_note
        except ConceptNote.DoesNotExist:
            return Response(
                {'error': 'No concept note for this topic yet.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        if not note.is_active:
            return Response(
                {'error': 'No concept note for this topic yet.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response({
            'topic_id': topic.id,
            'topic': topic.name,
            'subject': topic.subject.name,
            'title': note.title,
            'body': note.body,
            'updated_at': note.updated_at,
        })
