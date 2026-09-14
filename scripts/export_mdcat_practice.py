"""Export MDCAT standalone practice questions (past_paper=NULL, not in any
MockTest) for one or more subjects, for pushing to another environment.

Content-matched on the import side (question_text + option_a), so it's
safe to export "everything in this subject" even if some of it already
exists on the target — the import will just skip those.

Usage (from backend/, venv active):
    python scripts/export_mdcat_practice.py --subjects English Physics --output mdcat_practice_export.json
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
    ap.add_argument("--subjects", nargs="+", required=True,
                     help='e.g. --subjects English Physics')
    ap.add_argument("--exam", default="MDCAT")
    ap.add_argument("--output", default="mdcat_practice_export.json")
    opts = ap.parse_args()

    mock_ids = set()
    for m in MockTest.objects.all():
        mock_ids.update(m.questions.values_list("id", flat=True))

    qs = (
        Question.objects.filter(
            past_paper__isnull=True,
            subtopic__topic__subject__exam__name=opts.exam,
            subtopic__topic__subject__name__in=opts.subjects,
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
    print(f"Exported {len(rows)} questions ({', '.join(opts.subjects)}) -> {out_path.resolve()}")


if __name__ == "__main__":
    main()
