"""Export explanations for mocks 10-16 keyed by (question_text, option_a)
instead of id, so they can be loaded on a DB where these questions exist
under different PKs (e.g. production, via load_explanations_by_content).

Usage (from backend/, venv active):
    python scripts/export_mock_explanations_by_content.py 10 11 12 13 14 15 16
Writes one combined JSON to scripts/mock_10_16_explanations_by_content.json
"""
import json
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from quiz.models import MockTest

def main(nums):
    out = []
    for n in nums:
        try:
            mt = MockTest.objects.get(name=f"MDCAT Mock {n}", kind="full")
        except MockTest.DoesNotExist:
            print(f"MockTest 'MDCAT Mock {n}' not found, skipping")
            continue
        qs = mt.questions.all()
        count = 0
        for q in qs:
            out.append({
                "question_text": q.question_text,
                "option_a": q.option_a,
                "short": q.explanation_short,
                "long": q.explanation_long,
                "trick": q.explanation_trick,
                "options": q.explanation_options,
            })
            count += 1
        print(f"Mock {n}: exported {count} questions")

    out_path = ROOT / "scripts" / "mock_10_16_explanations_by_content.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} entries to {out_path}")


if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or list(range(10, 17))
    main(nums)
