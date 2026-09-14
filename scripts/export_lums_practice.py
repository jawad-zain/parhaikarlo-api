"""One-off: export the LUMS Math/Verbal standalone practice questions that
exist on production but not local, so they can be imported back to local.

Exports ALL fields needed to recreate the questions (including the content
hierarchy path and cached explanations), matched by content later, not PK.

Usage (from backend/, venv active, ON PRODUCTION):
    python scripts/export_lums_practice.py --output lums_practice_export.json
"""
import argparse
import json
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question  # noqa: E402
from quiz.models import MockTest  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="lums_practice_export.json")
    opts = ap.parse_args()

    mock_ids = set()
    for m in MockTest.objects.all():
        mock_ids.update(m.questions.values_list("id", flat=True))

    qs = (
        Question.objects.filter(
            is_active=True,
            past_paper__isnull=True,
            subtopic__topic__subject__exam__name="LUMS",
            subtopic__topic__subject__name__in=["Math", "Verbal"],
        )
        .exclude(id__in=mock_ids)
        .select_related("subtopic__topic__subject__exam")
    )

    rows = []
    for q in qs:
        st = q.subtopic
        tp = st.topic
        sj = tp.subject
        ex = sj.exam
        rows.append({
            "exam": ex.name,
            "subject": sj.name,
            "topic": tp.name,
            "subtopic": st.name,
            "question_text": q.question_text,
            "option_a": q.option_a,
            "option_b": q.option_b,
            "option_c": q.option_c,
            "option_d": q.option_d,
            "correct_answer": q.correct_answer,
            "difficulty": q.difficulty,
            "is_verified": q.is_verified,
            "is_active": q.is_active,
            "explanation_short": q.explanation_short,
            "explanation_long": q.explanation_long,
            "explanation_trick": q.explanation_trick,
            "explanation_options": q.explanation_options,
        })

    out_path = Path(opts.output)
    out_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported {len(rows)} questions -> {out_path.resolve()}")


if __name__ == "__main__":
    main()
