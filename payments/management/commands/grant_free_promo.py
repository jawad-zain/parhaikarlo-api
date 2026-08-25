import re

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from accounts.models import is_guest
from content.models import Exam
from payments.models import Subscription, SubscriptionPlan


PROMO_PLAN_NAME = 'Free Promo - First 30'

# Matches the throwaway QA/test accounts this project accumulates in every
# env (test@example.com, qa-test-*, claimtest_*, pwtest3_*, verify_*,
# test+mobile...@example.com, anything @example.com, etc.) so a promo run
# doesn't burn free slots on them instead of real students.
TEST_EMAIL_PATTERN = re.compile(
    r'(^test[+.@]|[+.]test|@example\.com$|^(qa|pwtest|claimtest|claimflow|verify)[-_])',
    re.IGNORECASE,
)


def looks_like_test_email(email):
    return bool(TEST_EMAIL_PATTERN.search(email or ''))


class Command(BaseCommand):
    help = (
        "Grant a free, non-purchasable subscription to the first N real "
        "(non-guest) signups for an exam, so they get the same access as a "
        "paid subscriber without going through payments. Idempotent — "
        "re-running only tops up users who don't already hold an active "
        "subscription, and never grants a second promo subscription to "
        "someone who already has one."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--exam', default='MDCAT',
            help="Exam name to grant access to (default: MDCAT).",
        )
        parser.add_argument(
            '--count', type=int, default=30,
            help="How many of the earliest signups to grant (default: 30).",
        )
        parser.add_argument(
            '--duration-days', type=int, default=90,
            help="Length of the free subscription in days (default: 90, "
                 "matching the paid 3-month plan).",
        )
        parser.add_argument(
            '--dry-run', action='store_true',
            help="Show who would be granted access without writing anything.",
        )
        parser.add_argument(
            '--include-test-emails', action='store_true',
            help="Don't filter out obvious QA/test accounts (test@, qa-*, "
                 "*@example.com, etc.) — off by default so promo slots go "
                 "to real signups.",
        )

    def handle(self, *args, **opts):
        exam = Exam.objects.filter(name=opts['exam'], is_active=True).first()
        if not exam:
            self.stderr.write(self.style.ERROR(f"No active exam named {opts['exam']!r}."))
            return

        count = opts['count']
        duration_days = opts['duration_days']

        plan, created = SubscriptionPlan.objects.get_or_create(
            exam=exam,
            name=PROMO_PLAN_NAME,
            defaults={
                'duration_days': duration_days,
                'price': 0,
                # Never shown on the public upgrade screen (SubscriptionPlanListView
                # filters on is_active=True) — this plan exists only so promo
                # subscriptions have somewhere to point.
                'is_active': False,
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Created promo plan {plan!r}.'))

        # Real signups only — guests (accounts.models.is_guest) are throwaway
        # rows created to let a visitor start a free paper without signing up,
        # not students who "signed up".
        from django.contrib.auth import get_user_model
        User = get_user_model()
        candidates = User.objects.filter(profile__primary_exam=exam).order_by('date_joined')
        real_signups = [u for u in candidates if not is_guest(u)]

        excluded_test = []
        if not opts['include_test_emails']:
            filtered = []
            for u in real_signups:
                if looks_like_test_email(u.email):
                    excluded_test.append(u)
                else:
                    filtered.append(u)
            real_signups = filtered

        real_signups = real_signups[:count]

        if excluded_test:
            self.stdout.write(f'Excluded {len(excluded_test)} test/QA-looking account(s):')
            for u in excluded_test:
                self.stdout.write(f'  SKIP   {u.email or u.username}  (looks like a test account)')

        self.stdout.write(f'{len(real_signups)} of the first {count} real signups for {exam.name}:')

        granted, skipped = [], []
        now = timezone.now()
        for user in real_signups:
            already_active = user.subscriptions.filter(
                plan__exam=exam,
                status='active',
                expires_at__gt=now,
            ).exists()
            if already_active:
                skipped.append(user)
                continue
            granted.append(user)

        for user in granted:
            self.stdout.write(f'  GRANT  {user.email or user.username}')
        for user in skipped:
            self.stdout.write(f'  SKIP   {user.email or user.username}  (already has an active subscription)')

        if opts['dry_run']:
            self.stdout.write(self.style.WARNING('Dry run — nothing written.'))
            return

        with transaction.atomic():
            for user in granted:
                Subscription.objects.create(
                    user=user,
                    plan=plan,
                    starts_at=now,
                    expires_at=now + timezone.timedelta(days=duration_days),
                    status='active',
                )

        self.stdout.write(self.style.SUCCESS(
            f'Granted free {duration_days}-day access to {len(granted)} student(s); '
            f'{len(skipped)} already covered.'
        ))
