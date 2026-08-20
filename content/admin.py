from django.contrib import admin
from .models import Exam, Subject, Topic, Subtopic, PastPaper, Question, ConceptNote
from .models import PastPaper, Question
from .models import Exam, Subject, Topic, Subtopic


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'board', 'level', 'is_active', 'created_at')
    list_filter = ('board', 'level', 'is_active')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam', 'weight_percent', 'question_count', 'order', 'is_active')
    list_filter = ('exam', 'is_active')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order', 'is_active')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'order', 'is_active')
    list_filter = ('subject__exam', 'subject', 'is_active')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order', 'is_active')
    autocomplete_fields = ('subject',)


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'order', 'is_active')
    list_filter = ('topic__subject__exam', 'topic__subject', 'is_active')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('order', 'is_active')
    autocomplete_fields = ('topic',)

@admin.register(PastPaper)
class PastPaperAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam', 'year', 'is_free', 'is_active', 'student_note', 'has_notes')
    list_filter = ('exam', 'year', 'is_free', 'is_active')
    search_fields = ('name', 'slug', 'notes', 'student_note')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_free', 'is_active')

    def has_notes(self, obj):
        return bool(obj.notes)
    has_notes.boolean = True
    has_notes.short_description = 'Has notes'


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'subtopic', 'past_paper', 'difficulty', 'correct_answer', 'is_verified', 'has_cached_explanation', 'is_active')
    list_editable = ('is_verified',)
    list_filter = (
        'subtopic__topic__subject__exam',
        'subtopic__topic__subject',
        'difficulty',
        'is_verified',
        'past_paper',
        'is_active',
    )
    search_fields = ('question_text', 'option_a', 'option_b', 'option_c', 'option_d')
    autocomplete_fields = ('subtopic', 'past_paper')
    readonly_fields = ('created_at', 'updated_at', 'explanation_generated_at')

    fieldsets = (
        ('Classification', {
            'fields': ('subtopic', 'past_paper', 'difficulty', 'is_active')
        }),
        ('Question', {
            'fields': ('question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer')
        }),
        ('AI explanation cache', {
            'fields': ('explanation_short', 'explanation_long', 'explanation_trick', 'explanation_generated_at'),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Question')
    def short_text(self, obj):
        return obj.question_text[:80] + ('...' if len(obj.question_text) > 80 else '')
@admin.register(ConceptNote)
class ConceptNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'version', 'is_indexed', 'is_active', 'updated_at')
    list_filter = ('topic__subject__exam', 'topic__subject', 'is_indexed', 'is_active')
    search_fields = ('title', 'body')
    autocomplete_fields = ('topic',)
    readonly_fields = ('version', 'is_indexed', 'created_at', 'updated_at')        