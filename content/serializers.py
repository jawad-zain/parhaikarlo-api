from rest_framework import serializers
from django.db.models import Count, Q
from .models import Exam, PastPaper


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