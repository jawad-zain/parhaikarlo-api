"""One-off: attach the 24 LUMS LCAT sample questions to a real PastPaper row.

Context: these 24 questions were originally imported (2026-09-08) as a
standalone practice bank with past_paper=NULL, per lums-content/README.md's
original decision ("don't invent a fake year to force it into a PastPaper").
2026-09-09: the user explicitly asked for this to go through the same
pipeline as MDCAT past papers/mocks instead — content-verify by reasoning
(same as mocks, which also have no external answer key) and expose it as a
named past paper. This script does the attach step of that.

Mirrors the mock-test attach_mockN.py pattern (get_or_create + match by
(question_text, option_a) + paper_order from source question_number) rather
than relying on import_mcqs.py's auto-create-by-year path, which would name
the paper "LUMS 2025" instead of the name we actually want.

Idempotent: safe to re-run.
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

from content.models import Exam, PastPaper, Question  # noqa: E402

JSON_PATH = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_LCAT_SAMPLE.json"


def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8-sig"))
    exam = Exam.objects.get(slug="lums")

    paper, created = PastPaper.objects.get_or_create(
        exam=exam,
        slug="lums-sample-past-paper",
        defaults={
            "name": "LUMS Sample Past Paper",
            "year": 2025,
            "is_free": True,
            "is_active": True,
            "notes": (
                "Source: LUMS' own official 'Sample Questions for Verbal & Math "
                "Sections' guide (lums-content/raw-sources/sample_lcat_2025.pdf), "
                "not a dated official past paper and no official answer key was "
                "released for it. Answers were reasoned from question content "
                "(grammar/logic for Verbal, calculation for Math), then "
                "independently content-verified by Claude on 2026-09-09 "
                "(0 errors found across all 24) before is_verified was set True "
                "— same treatment as MDCAT mock tests, which also carry no "
                "external key."
            ),
        },
    )
    print(f"PastPaper: {'created' if created else 'already existed'} — id={paper.id} name={paper.name!r}")

    matched = 0
    for mcq in data:
        q = Question.objects.filter(
            subtopic__topic__subject__exam=exam,
            past_paper__isnull=True,
            question_text=mcq["question_text"],
            option_a=mcq["options"]["a"],
        ).first()
        if not q:
            print(f"  MISSING match for question_number={mcq['question_number']}: {mcq['question_text'][:60]!r}")
            continue
        q.past_paper = paper
        q.paper_order = mcq["question_number"]
        q.save(update_fields=["past_paper", "paper_order"])
        matched += 1

    print(f"Attached {matched}/{len(data)} questions to {paper.name!r}")


if __name__ == "__main__":
    main()
