from django.db import models


class BuildTask(models.Model):
    """One item on the 12-week build plan. Ticked off from admin."""

    week = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True, default='')
    is_done = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['week', 'order', 'id']

    def __str__(self):
        check = '✓' if self.is_done else '·'
        return f'W{self.week} {check} {self.title}'