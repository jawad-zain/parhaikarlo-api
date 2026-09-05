"""Export explanations for practice-bank questions keyed by (question_text,
option_a) instead of id, so they can be loaded on a DB where these questions
exist under different PKs (e.g. production, via load_explanations_by_content).

Unlike export_mock_explanations_by_content.py (which walks a MockTest's
`questions` M2M), practice-bank questions have no such grouping — so this
script takes a "keys" JSON (a list of {"question_text", "option_a"} produced
from the bank's parsed-mcqs JSON) and looks each one up directly.

Usage (from backend/, venv active):
    python scripts/export_practice_explanations_by_content.py <keys.json> <out.json>
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

from content.models import Question


def main(keys_path, out_path):
    keys = json.loads(Path(keys_path).read_text(encoding="utf-8"))
    out = []
    missing = 0
    for k in keys:
        q = Question.objects.filter(
            past_paper__isnull=True,
            question_text=k["question_text"],
            option_a=k["option_a"],
        ).first()
        if not q:
            missing += 1
            continue
        out.append({
            "question_text": q.question_text,
            "option_a": q.option_a,
            "short": q.explanation_short,
            "long": q.explanation_long,
            "trick": q.explanation_trick,
            "options": q.explanation_options,
        })

    Path(out_path).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Exported {len(out)} explanations, {missing} keys not found locally, to {out_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
