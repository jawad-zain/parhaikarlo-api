"""Unlock every paper and mock, and stop selling plans while access is free.

Launch-phase decision (2026-09-17): nothing on ParhaiKrlo is paid, so no
card may show a lock, a "Premium" badge or a buyable plan.

Three things have to agree or the site contradicts itself:

  * FREE_LAUNCH_MODE (settings) already bypasses the subscription check for
    signed-up users, but is_free=False still put a lock on the card and
    forced a guest to sign up first.
  * PastPaper.is_free / MockTest.is_free drive the badges, the lock icon and
    the guest path.
  * An active SubscriptionPlan keeps /plans selling access that every
    account already has.

Nothing is deleted: existing Subscription rows and the plans themselves stay
in the database, so flipping any of this back is an is_active update.

    py -3.14 scripts/make_everything_free.py            # dry run
    py -3.14 scripts/make_everything_free.py --apply

Idempotent — a second run reports nothing to do.
"""
import os
import sys

import django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from content.models import PastPaper          # noqa: E402
from payments.models import SubscriptionPlan  # noqa: E402
from quiz.models import MockTest              # noqa: E402

apply_changes = '--apply' in sys.argv

papers = PastPaper.objects.filter(is_free=False)
mocks = MockTest.objects.filter(is_free=False)
plans = SubscriptionPlan.objects.filter(is_active=True)

print(f"papers to unlock: {papers.count()}")
for p in papers.order_by('exam__slug', 'year'):
    print(f"  {p.exam.slug} {p.year} — {p.name}")
print(f"mocks to unlock: {mocks.count()}")
for m in mocks.order_by('exam__slug', 'name'):
    print(f"  {m.exam.slug} — {m.name}")
print(f"plans to deactivate: {plans.count()}")
for pl in plans:
    print(f"  {pl.name}")

if not apply_changes:
    print("\nDry run — nothing written. Re-run with --apply.")
    sys.exit(0)

print(f"\nunlocked papers: {papers.update(is_free=True)}")
print(f"unlocked mocks: {mocks.update(is_free=True)}")
print(f"deactivated plans: {plans.update(is_active=False)}")
print(
    "locked left: "
    f"{PastPaper.objects.filter(is_free=False).count()} papers, "
    f"{MockTest.objects.filter(is_free=False).count()} mocks, "
    f"{SubscriptionPlan.objects.filter(is_active=True).count()} active plans"
)
