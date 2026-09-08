"""One-off: mark all LUMS Sample Past Paper questions is_verified=True.

Run AFTER scripts/attach_lums_sample.py. Separated out (rather than folded
into the attach script) because the verification claim itself — "Claude
content-checked all 24 answers by hand on 2026-09-09, zero errors" — isn't
re-derivable from any source file the way the attach step is; this script
just applies that already-made decision to whichever DB it's run against
(local or production). Idempotent.

See lums-content/README.md's 2026-09-09 update for the reasoning.
"""
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question  # noqa: E402


def main():
    qs = Question.objects.filter(past_paper__slug="lums-sample-past-paper")
    n = qs.update(is_verified=True)
    print(f"is_verified=True set on {n} questions "
          f"({qs.filter(is_verified=True).count()}/{qs.count()} now verified)")


if __name__ == "__main__":
    main()
