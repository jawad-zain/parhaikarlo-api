from django.conf import settings
from django.db import models


class StudentProfile(models.Model):
    CLASS_CHOICES = [
        ('fsc1', 'FSc Part 1'),
        ('fsc2', 'FSc Part 2'),
        ('repeater', 'Repeater'),
        ('matric', 'Matric'),
        ('other', 'Other'),
    ]
    BREAK_INTERVAL_CHOICES = [(40, '40 min'), (60, '60 min'), (90, '90 min')]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    primary_exam = models.ForeignKey(
        'content.Exam',
        on_delete=models.PROTECT,
        related_name='students',
    )
    full_name = models.CharField(max_length=120)
    city = models.CharField(max_length=60, blank=True)
    current_class = models.CharField(max_length=20, choices=CLASS_CHOICES, blank=True)
    target_year = models.PositiveSmallIntegerField(null=True, blank=True)

    # The actual exam day, as the student knows it (roll number slip,
    # official notice, etc.) — powers the test-date pacing plan.
    # target_year above is coarser and kept only for backward compat.
    target_date = models.DateField(null=True, blank=True)

    phone = models.CharField(max_length=15, blank=True)
    is_email_verified = models.BooleanField(default=False)
    preferred_break_interval_minutes = models.PositiveSmallIntegerField(
        default=40, choices=BREAK_INTERVAL_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name} ({self.user.email if self.user.email else self.user.username})'