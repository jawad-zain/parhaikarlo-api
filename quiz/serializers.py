from rest_framework import serializers

from content.models import Question, QuestionImage
from .models import Attempt, AttemptQuestion


class QuestionImageSerializer(serializers.ModelSerializer):
    """
    Returns the visual(s) attached to a question.

    Normal question:
        "images": []

    Visual question:
        "images": [
            {
                "id": 1,
                "image": "http://127.0.0.1:8000/media/question_images/...",
                "source_name": "MDCAT 2016",
                "source_year": 2016,
                "page_number": null
            }
        ]
    """

    class Meta:
        model = QuestionImage
        fields = [
            'id',
            'image',
            'source_name',
            'source_year',
            'page_number',
        ]


class QuestionListSerializer(serializers.ModelSerializer):
    """For GET /questions — the browsable list. No correct answer leaked."""

    subject = serializers.CharField(
        source='subtopic.topic.subject.name',
        read_only=True,
    )
    topic = serializers.CharField(
        source='subtopic.topic.name',
        read_only=True,
    )
    subtopic = serializers.CharField(
        source='subtopic.name',
        read_only=True,
    )

    images = QuestionImageSerializer(
        many=True,
        read_only=True,
    )

    is_visual_required = serializers.BooleanField(
        read_only=True,
    )

    class Meta:
        model = Question
        fields = [
            'id',
            'question_text',
            'option_a',
            'option_b',
            'option_c',
            'option_d',
            'difficulty',
            'subject',
            'topic',
            'subtopic',
            'is_visual_required',
            'images',
        ]


class AttemptQuestionSerializer(serializers.ModelSerializer):
    """
    For serving a Q inside an attempt.

    Still does NOT expose correct_answer or is_correct.
    """

    question_text = serializers.CharField(
        source='question.question_text',
        read_only=True,
    )
    option_a = serializers.CharField(
        source='question.option_a',
        read_only=True,
    )
    option_b = serializers.CharField(
        source='question.option_b',
        read_only=True,
    )
    option_c = serializers.CharField(
        source='question.option_c',
        read_only=True,
    )
    option_d = serializers.CharField(
        source='question.option_d',
        read_only=True,
    )
    difficulty = serializers.CharField(
        source='question.difficulty',
        read_only=True,
    )

    is_visual_required = serializers.BooleanField(
        source='question.is_visual_required',
        read_only=True,
    )

    images = QuestionImageSerializer(
        source='question.images',
        many=True,
        read_only=True,
    )

    class Meta:
        model = AttemptQuestion
        fields = [
            'id',
            'order_in_attempt',
            'question_text',
            'option_a',
            'option_b',
            'option_c',
            'option_d',
            'difficulty',
            'selected_option',
            'is_visual_required',
            'images',
        ]


class AttemptCreateSerializer(serializers.Serializer):
    """For POST /attempts — validates the request payload."""

    exam_id = serializers.IntegerField()

    subject_id = serializers.IntegerField(
        required=False,
        allow_null=True,
    )

    topic_id = serializers.IntegerField(
        required=False,
        allow_null=True,
    )

    difficulty = serializers.ChoiceField(
        choices=['easy', 'medium', 'hard'],
        required=False,
        allow_null=True,
    )

    limit = serializers.IntegerField(
        default=20,
        min_value=1,
        max_value=50,
    )


class AttemptDetailSerializer(serializers.ModelSerializer):
    """For POST /attempts response — returns attempt + questions."""

    items = AttemptQuestionSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Attempt
        fields = [
            'id',
            'mode',
            'total_questions',
            'started_at',
            'is_completed',
            'items',
        ]


class AnswerSubmitSerializer(serializers.Serializer):
    """For POST /attempts/<id>/answer — validates answer payload."""

    attempt_question_id = serializers.IntegerField()

    selected_option = serializers.ChoiceField(
        choices=['a', 'b', 'c', 'd'],
    )

    time_spent_seconds = serializers.IntegerField(
        min_value=0,
        max_value=3600,
    )