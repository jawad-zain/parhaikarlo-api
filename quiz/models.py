from django.conf import settings
from django.db import models


class Attempt(models.Model):
    MODE_CHOICES = [
        ('practice', 'Practice'),
        ('mock', 'Mock Test'),
        ('past_paper', 'Past Paper'),
        ('sectional', 'Sectional Mock'),
    ]
    DEVICE_CHOICES = [
        ('desktop', 'Desktop'),
        ('mobile', 'Mobile'),
        ('tablet', 'Tablet'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='attempts',
    )

    mock_test = models.ForeignKey(
        'MockTest', null=True, blank=True,
        on_delete=models.PROTECT, related_name='attempts',
    )
    mode = models.CharField(max_length=15, choices=MODE_CHOICES)
    exam = models.ForeignKey('content.Exam', on_delete=models.PROTECT)
    subject = models.ForeignKey(
        'content.Subject', null=True, blank=True, on_delete=models.PROTECT,
    )
    topic = models.ForeignKey(
        'content.Topic', null=True, blank=True, on_delete=models.PROTECT,
    )
    subtopic = models.ForeignKey(
        'content.Subtopic', null=True, blank=True, on_delete=models.PROTECT,
    )
    past_paper = models.ForeignKey(
        'content.PastPaper', null=True, blank=True, on_delete=models.PROTECT,
    )

    # Timing
    started_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)  # mocks only
    submitted_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    # Cached results (filled on submit)
    total_questions = models.PositiveIntegerField(default=0)
    correct_count = models.PositiveIntegerField(default=0)
    score_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
    )

    # Week 5+ fields — adding now with defaults so no future migration
    allow_breaks = models.BooleanField(default=True)
    integrity_flagged = models.BooleanField(default=False)
    device_class = models.CharField(max_length=10, choices=DEVICE_CHOICES, default='desktop')

    class Meta:
        indexes = [
            models.Index(fields=['user', '-started_at']),
            models.Index(fields=['mode', '-started_at']),
        ]
        ordering = ['-started_at']

    def __str__(self):
        return f'{self.user} - {self.mode} - {self.started_at:%Y-%m-%d %H:%M}'


class AttemptQuestion(models.Model):
    OPTION_CHOICES = [('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')]

    attempt = models.ForeignKey(
        Attempt, on_delete=models.CASCADE, related_name='items',
    )
    question = models.ForeignKey('content.Question', on_delete=models.PROTECT)
    order_in_attempt = models.PositiveSmallIntegerField()

    selected_option = models.CharField(
        max_length=1, choices=OPTION_CHOICES, null=True, blank=True,
    )
    is_correct = models.BooleanField(null=True)  # null = unanswered
    time_spent_seconds = models.PositiveIntegerField(default=0)
    answered_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = [
            ('attempt', 'question'),        # same Q can't appear twice in one attempt
            ('attempt', 'order_in_attempt'), # each order slot unique
        ]
        ordering = ['order_in_attempt']

    def __str__(self):
        return f'{self.attempt_id}: Q{self.order_in_attempt}'


class AttemptViolation(models.Model):
    VIOLATION_CHOICES = [
        ('tab_hidden', 'Tab Hidden'),
        ('window_blur', 'Window Blur'),
        ('fullscreen_exit', 'Fullscreen Exit'),
        ('copy_attempt', 'Copy Attempt'),
    ]

    attempt = models.ForeignKey(
        Attempt,
        on_delete=models.CASCADE,
        related_name='violations',
    )
    violation_type = models.CharField(
        max_length=30,
        choices=VIOLATION_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['attempt', 'created_at']),
        ]

    def __str__(self):
        return f'Attempt {self.attempt_id} — {self.violation_type}'

class MockTest(models.Model):
    """A pre-configured mock test template. Students pick one to take;
    each attempt is a separate Attempt row with mode='mock' or 'sectional'.
    """

    KIND_CHOICES = [
        ('full', 'Full Mock'),           # 200 Q, all subjects, MDCAT weightage
        ('sectional', 'Sectional Mock'), # 60 Q, one subject
    ]

    exam = models.ForeignKey(
        'content.Exam', on_delete=models.CASCADE, related_name='mock_tests',
    )
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=15, choices=KIND_CHOICES)
    # Only set for kind='sectional'.
    subject = models.ForeignKey(
        'content.Subject', null=True, blank=True,
        on_delete=models.PROTECT, related_name='sectional_mocks',
    )
    duration_minutes = models.PositiveSmallIntegerField()  # 210 full, 45 sectional
    total_questions = models.PositiveSmallIntegerField()   # 200 full, 60 sectional

    # Optional fixed question set for kind='full' mocks — e.g. a distinct
    # authored "paper" (Mock Test 2, 3, ...) rather than a fresh random draw.
    # If empty, create_mock_attempt() falls back to the original behaviour:
    # select_questions_for_full_mock() weighted-random-samples the whole
    # verified Question pool for the exam. If populated, that exact set is
    # used (in paper_order) every time this MockTest is attempted.
    questions = models.ManyToManyField(
        'content.Question', blank=True, related_name='fixed_in_mock_tests',
    )

    # 1 free full mock + 2 free sectional per subject.
    is_free = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['exam', 'kind', 'name']

    def __str__(self):
        return f'{self.exam.name} — {self.name} ({self.kind})'


# Add this FK to the existing Attempt model class. Don't create a new Attempt class.
# I'll show the diff separately below.        

class UserProgress(models.Model):
    """Per-user, per-subject syllabus coverage snapshot.

    Recomputed inside finalize_attempt on submit — dashboard reads this row
    directly, no aggregation on page load. One row per (user, subject).
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progress',
    )
    subject = models.ForeignKey(
        'content.Subject',
        on_delete=models.CASCADE,
        related_name='user_progress',
    )

    # Coverage = distinct subtopics attempted / total subtopics in subject.
    coverage_pct = models.FloatField(default=0)
    subtopics_attempted = models.PositiveIntegerField(default=0)
    subtopics_total = models.PositiveIntegerField(default=0)  # snapshot at compute time

    # All-time totals for this user in this subject.
    questions_attempted = models.PositiveIntegerField(default=0)
    accuracy_pct = models.FloatField(default=0)  # correct / attempted

    last_computed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('user', 'subject')]
        ordering = ['user', 'subject']

    def __str__(self):
        return f'{self.user} · {self.subject.name} · {self.coverage_pct:.0f}%'