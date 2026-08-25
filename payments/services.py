import logging
import re

from django.db import transaction
from django.utils import timezone

from accounts.models import is_guest
from payments.models import Subscription, SubscriptionPlan, has_active_subscription

logger = logging.getLogger(__name__)

PROMO_PLAN_NAME = 'Free Promo - First 30'
PROMO_SLOT_COUNT = 30
PROMO_DURATION_DAYS = 90  # matches the paid 3-month plan

# Matches the throwaway QA/test accounts this project accumulates in every
# env (test@example.com, qa-test-*, claimtest_*, pwtest3_*, verify_*,
# test+mobile...@example.com, anything @example.com, etc.) so a promo grant
# doesn't burn free slots on them instead of real students. Shared by the
# manual command (grant_free_promo) and the automatic signup-time grant
# below — one definition, one place to update.
TEST_EMAIL_PATTERN = re.compile(
    r'(^test[+.@]|[+.]test|@example\.com$|^(qa|pwtest|claimtest|claimflow|verify)[-_])',
    re.IGNORECASE,
)


def looks_like_test_email(email):
    return bool(TEST_EMAIL_PATTERN.search(email or ''))


def get_or_create_promo_plan(exam, duration_days=PROMO_DURATION_DAYS):
    """The non-purchasable SubscriptionPlan promo subscriptions point to.
    Never shown on the public upgrade screen (SubscriptionPlanListView
    filters on is_active=True) — it exists only so promo Subscription rows
    have a plan to reference.
    """
    plan, _ = SubscriptionPlan.objects.get_or_create(
        exam=exam,
        name=PROMO_PLAN_NAME,
        defaults={
            'duration_days': duration_days,
            'price': 0,
            'is_active': False,
        },
    )
    return plan


def grant_free_promo_if_eligible(user, exam, count=PROMO_SLOT_COUNT, duration_days=PROMO_DURATION_DAYS):
    """Grant `user` a free `duration_days`-long Subscription for `exam` if
    they're one of the first `count` real signups to receive this promo.

    Returns the created Subscription, or None if `user` isn't eligible (a
    guest, a test-looking email, already covered by an active subscription)
    or the `count` slots for this exam are already used up.

    Concurrency-safe: locks the promo plan row (SELECT ... FOR UPDATE) for
    the duration of the count-check + insert, so two signups racing for the
    last slot can't both read "29 granted" and both insert a 30th.

    Callers are responsible for isolating failures — this can raise (DB
    errors etc.) and deliberately doesn't swallow them itself, so a caller
    that must not fail (e.g. mid-signup) should wrap the call in its own
    try/except.
    """
    if is_guest(user):
        return None
    if looks_like_test_email(user.email):
        return None
    if has_active_subscription(user, exam):
        return None

    with transaction.atomic():
        plan = get_or_create_promo_plan(exam, duration_days)
        # Lock the plan row so a concurrent call for the same exam blocks
        # here until this transaction commits or rolls back — that's what
        # makes the count check below race-safe.
        plan = SubscriptionPlan.objects.select_for_update().get(pk=plan.pk)

        if Subscription.objects.filter(plan=plan).count() >= count:
            return None

        # Re-check under the lock — someone else (e.g. the manual command,
        # or another request for this same user) may have granted an active
        # subscription between the has_active_subscription() check above
        # and acquiring the lock.
        if has_active_subscription(user, exam):
            return None

        now = timezone.now()
        return Subscription.objects.create(
            user=user,
            plan=plan,
            starts_at=now,
            expires_at=now + timezone.timedelta(days=duration_days),
            status='active',
        )


def grant_free_promo_if_eligible_silently(user, exam, count=PROMO_SLOT_COUNT, duration_days=PROMO_DURATION_DAYS):
    """Same as grant_free_promo_if_eligible(), but never raises — logs and
    returns None on failure instead. Use this at signup time, where a promo
    hiccup must never fail registration; the manual `grant_free_promo`
    command is the safety net for anyone missed this way.
    """
    try:
        return grant_free_promo_if_eligible(user, exam, count=count, duration_days=duration_days)
    except Exception:
        logger.exception(
            'grant_free_promo_if_eligible failed for user_id=%s exam_id=%s — '
            'registration continues; grant_free_promo command will catch this later.',
            getattr(user, 'pk', None), getattr(exam, 'pk', None),
        )
        return None
