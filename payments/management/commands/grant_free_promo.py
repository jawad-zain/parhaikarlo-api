from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from accounts.models import is_guest
from content.models import Exam
from payments.models import has_active_subscription
from payments.services import (
    PROMO_DURATION_DAYS,
    PROMO_SLOT_COUNT,
    grant_free_promo_if_eligible,
    looks_like_test_email,
)


class Command(BaseCommand):
    help = (
        "Grant a free, non-purchasable subscription to the first N real "
        "(non-guest) signups for an exam, so they get the same access as a "
        "paid subscriber without going through payments. Idempotent — "
        "re-running only tops up users who don't already hold an active "
        "subscription. This is the manual safety net for the automatic "
        "grant that runs at signup (see payments.services) — use it to "
        "catch anyone the automatic path missed (e.g. it errored, or was "
        "deployed after they signed up)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--exam', default='MDCAT',
            help="Exam name to grant access to (default: MDCAT).",
        )
        parser.add_argument(
            '--count', type=int, default=PROMO_SLOT_COUNT,
            help=f"How many of the earliest signups to grant (default: {PROMO_SLOT_COUNT}).",
        )
        parser.add_argument(
            '--duration-days', type=int, default=PROMO_DURATION_DAYS,
            help=f"Length of the free subscription in days (default: {PROMO_DURATION_DAYS}, "
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

        User = get_user_model()
        candidates = User.objects.filter(profile__primary_exam=exam).order_by('date_joined')
        real_signups = [u for u in candidates if not is_guest(u)]

        excluded_test = []
        if not opts['include_test_emails']:
            filtered, excluded_test = [], []
            for u in real_signups:
                (excluded_test if looks_like_test_email(u.email) else filtered).append(u)
            real_signups = filtered

        if excluded_test:
            self.stdout.write(f'Excluded {len(excluded_test)} test/QA-looking account(s):')
            for u in excluded_test:
                self.stdout.write(f'  SKIP   {u.email or u.username}  (looks like a test account)')

        # Same "first N" ordering as the automatic grant would apply, so a
        # dry run here previews exactly what running for real would do.
        real_signups = real_signups[:count]
        self.stdout.write(f'{len(real_signups)} of the first {count} real signups for {exam.name}:')

        if opts['dry_run']:
            already_covered = 0
            for user in real_signups:
                if has_active_subscription(user, exam):
                    self.stdout.write(f'  SKIP   {user.email or user.username}  (already has an active subscription)')
                    already_covered += 1
                else:
                    self.stdout.write(f'  GRANT  {user.email or user.username}')
            self.stdout.write(self.style.WARNING(
                f'Dry run — nothing written. Would grant '
                f'{len(real_signups) - already_covered}, skip {already_covered} already-covered.'
            ))
            return

        granted, skipped = [], []
        for user in real_signups:
            sub = grant_free_promo_if_eligible(user, exam, count=count, duration_days=duration_days)
            if sub is not None:
                granted.append(user)
                self.stdout.write(f'  GRANT  {user.email or user.username}')
            else:
                skipped.append(user)
                self.stdout.write(f'  SKIP   {user.email or user.username}  (already covered, or slots exhausted)')

        self.stdout.write(self.style.SUCCESS(
            f'Granted free {duration_days}-day access to {len(granted)} student(s); '
            f'{len(skipped)} skipped.'
        ))
