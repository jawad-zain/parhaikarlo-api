from django.contrib import admin
from .models import Attempt, AttemptQuestion
from .models import UserProgress
from .models import MockTest

@admin.register(MockTest)
class MockTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam', 'kind', 'subject', 'duration_minutes',
                    'total_questions', 'is_free', 'is_active')
    list_filter = ('kind', 'is_free', 'is_active', 'exam')
    search_fields = ('name',)

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'coverage_pct', 'subtopics_attempted',
                    'subtopics_total', 'questions_attempted', 'accuracy_pct',
                    'last_computed')
    list_filter = ('subject',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('last_computed',)

class AttemptQuestionInline(admin.TabularInline):
    model = AttemptQuestion
    extra = 0
    fields = ('order_in_attempt', 'question', 'selected_option', 'is_correct', 'time_spent_seconds')
    readonly_fields = fields


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'mode', 'exam', 'subject',
        'total_questions', 'correct_count', 'score_percentage',
        'is_completed', 'integrity_flagged', 'started_at',
    )
    list_filter = ('mode', 'exam', 'is_completed', 'integrity_flagged', 'device_class')
    search_fields = ('user__email', 'user__username')
    readonly_fields = ('started_at', 'submitted_at', 'total_questions', 'correct_count', 'score_percentage')
    inlines = [AttemptQuestionInline]