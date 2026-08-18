
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import Question
from .services import generate_explanation


class QuestionExplainView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, question_id):
        question = get_object_or_404(
            Question,
            id=question_id,
            is_active=True,
            is_verified=True,
        )

        explanation = generate_explanation(question)

        return Response({
            "question_id": question.id,
            "explanation": explanation,
        })

class QuestionExplanationReportView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, question_id):
        question = get_object_or_404(
            Question,
            id=question_id,
            is_active=True,
            is_verified=True,
        )

        question.explanation_short = ''
        question.explanation_long = ''
        question.explanation_trick = ''
        question.explanation_generated_at = None

        question.save(
            update_fields=[
                'explanation_short',
                'explanation_long',
                'explanation_trick',
                'explanation_generated_at',
                'updated_at',
            ]
        )

        return Response({
            'question_id': question.id,
            'message': 'Explanation reported and cleared.',
        })