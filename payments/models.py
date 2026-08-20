from django.conf import settings
from django.db import models
from django.utils import timezone


def has_active_subscription(user, exam):
    """True if `user` currently holds a paid, non-expired subscription
    covering `exam`. Being signed up (not a guest) is NOT enough on its
    own — used alongside accounts.models.is_guest to gate non-free past
    papers/mocks (see quiz.views.PastPaperStartView / MockStartView).
    """
    if user.is_anonymous:
        return False
    return Subscription.objects.filter(
        user=user,
        plan__exam=exam,
        status='active',
        expires_at__gt=timezone.now(),
    ).exists()


class SubscriptionPlan(models.Model):
    """
    A configurable paid plan for an exam.

    Example:
    MDCAT — 6 Months
    MDCAT — 1 Month
    """

    exam = models.ForeignKey(
        'content.Exam',
        on_delete=models.PROTECT,
        related_name='subscription_plans',
    )

    name = models.CharField(max_length=100)

    duration_days = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['exam', 'price', 'duration_days']
        unique_together = [('exam', 'name')]

    def __str__(self):
        return f'{self.exam.name} — {self.name}'


class Subscription(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )

    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.PROTECT,
        related_name='subscriptions',
    )

    starts_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['expires_at']),
        ]

    def __str__(self):
        return f'{self.user} — {self.plan.name} — {self.status}'


class Payment(models.Model):
    # Only the two merchant accounts actually offered on the frontend
    # (app/(app)/plans/upgrade/[planId]/page.tsx METHODS array). Historical
    # 'manual'/'jazzcash'/'bank_transfer' rows from before this cutover keep
    # working (choices only validate new writes) but can no longer be picked.
    METHOD_CHOICES = [
        ('easypaisa', 'EasyPaisa'),
        ('sadapay', 'SadaPay'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('refunded', 'Refunded'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='payments',
    )

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.PROTECT,
        related_name='payments',
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES,
        default='easypaisa',
    )

    transaction_reference = models.CharField(
        max_length=150,
        blank=True,
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending',
    )

    proof_image = models.ImageField(
        upload_to='payment_proofs/',
        blank=True,
        null=True,
    )

    notes = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['status', '-created_at']),
        ]

    def __str__(self):
        return (
            f'{self.user} — {self.amount} — '
            f'{self.method} — {self.status}'
        )


class PaymentMethodOption(models.Model):
    """An admin-editable payment channel to offer on the upgrade screen —
    e.g. "EasyPaisa — Send to 0321-3529795 · Jawad Zain".

    Replaces what used to be hardcoded in the frontend
    (app/(app)/plans/upgrade/[planId]/page.tsx's METHODS array): the
    account number/name students send money to was compiled straight into
    the JS bundle, so changing it meant a frontend deploy. Now it's data —
    GET /api/payments/methods/ serves whatever's active here.
    """

    method = models.CharField(
        max_length=20,
        choices=Payment.METHOD_CHOICES,
        unique=True,
    )
    label = models.CharField(max_length=50)
    instructions = models.CharField(
        max_length=200,
        help_text="Shown to the student, e.g. 'Send to 0321-3529795 · Jawad Zain'.",
    )
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'method']

    def __str__(self):
        return f'{self.label} ({"active" if self.is_active else "inactive"})'