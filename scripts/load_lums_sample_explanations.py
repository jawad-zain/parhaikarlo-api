"""Load LUMS Sample Past Paper explanations, matched by (question_text,
option_a) rather than PK — content/management/commands/load_explanations_by_content.py
hardcodes past_paper__isnull=True (built for practice banks), which doesn't
match these questions once they're attached to a PastPaper. This is the same
idea, scoped to the LUMS sample paper specifically. Idempotent.

Usage: python scripts/load_lums_sample_explanations.py [path/to/explanations_by_content.json]
Defaults to scripts/lums_sample_explanations_by_content.json.
"""
import json
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.utils import timezone  # noqa: E402
from content.models import Question  # noqa: E402


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "scripts/lums_sample_explanations_by_content.json"
    items = json.loads(Path(path).read_text(encoding="utf-8"))

    updated = missing = 0
    for item in items:
        q = Question.objects.filter(
            past_paper__slug="lums-sample-past-paper",
            question_text=item["question_text"],
            option_a=item["option_a"],
        ).first()
        if not q:
            print(f"MISSING: {item['question_text'][:60]!r}")
            missing += 1
            continue
        q.explanation_short = item["short"]
        q.explanation_long = item["long"]
        q.explanation_trick = item["trick"]
        q.explanation_options = item["options"]
        q.explanation_generated_at = timezone.now()
        q.save(update_fields=[
            "explanation_short", "explanation_long", "explanation_trick",
            "explanation_options", "explanation_generated_at", "updated_at",
        ])
        updated += 1

    print(f"Updated {updated} questions. {missing} missing.")


if __name__ == "__main__":
    main()
