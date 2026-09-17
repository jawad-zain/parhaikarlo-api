from rest_framework import serializers
from django.db.models import Count, Q
from .models import Exam, PastPaper, QuestionReport


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'slug', 'board', 'level', 'is_active']


class PastPaperSerializer(serializers.ModelSerializer):
    """List view of past papers with question counts + difficulty breakdown."""

    question_count = serializers.IntegerField(read_only=True)
    verified_count = serializers.IntegerField(read_only=True)
    easy_count = serializers.IntegerField(read_only=True)
    medium_count = serializers.IntegerField(read_only=True)
    hard_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = PastPaper
        fields = [
            'id', 'name', 'slug', 'year', 'is_free', 'is_active',
            'question_count', 'verified_count',
            'easy_count', 'medium_count', 'hard_count',
            'student_note',
        ]


class QuestionReportSerializer(serializers.ModelSerializer):
    """Write-only: a report is filed, never read back by the student.

    `question` is the only required field. A report with no message is still
    worth having - it says "look at this one" - so `message` stays optional,
    and `email` is only there so we can reply.
    """

    class Meta:
        model = QuestionReport
        fields = ['id', 'question', 'kind', 'message', 'email']
        read_only_fields = ['id']

    def validate_question(self, value):
        if not value.is_active:
            # An inactive question is one we have already pulled, so there is
            # nothing to report - but say so rather than accepting silently.
            raise serializers.ValidationError('That question is not currently live.')
        return value

    def validate_message(self, value):
        return value.strip()[:4000]
