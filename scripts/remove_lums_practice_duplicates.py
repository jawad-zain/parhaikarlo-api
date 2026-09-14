"""One-off: remove the 24 standalone-practice questions on production that
are exact-content duplicates of PastPaper "LUMS 2025" questions (they were
accidentally double-created there — once attached to the paper, once again
as standalone practice under mis-tagged Subjects "Math"/"Verbal").

Matches ONLY questions that are:
  - standalone (past_paper IS NULL)
  - under Exam "LUMS", Subject in ("Math", "Verbal")
  - content-identical (question_text + option_a) to a question attached to
    PastPaper "LUMS 2025"
so it can never touch a genuine practice question that just happens to
share a subject name.

Usage (from backend/, venv active, ON PRODUCTION):
    python scripts/remove_lums_practice_duplicates.py --dry-run
    python scripts/remove_lums_practice_duplicates.py --apply
"""
import argparse
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question, PastPaper  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Actually deactivate the rows")
    ap.add_argument("--dry-run", action="store_true", help="Just report what would happen (default)")
    opts = ap.parse_args()

    paper = PastPaper.objects.filter(name__icontains="LUMS", year=2025).first()
    if not paper:
        print("Could not find the LUMS 2025 past paper — aborting.")
        return

    paper_signatures = set(
        paper.questions.values_list("question_text", "option_a")
    )
    print(f"LUMS 2025 paper has {len(paper_signatures)} question signatures.")

    candidates = Question.objects.filter(
        past_paper__isnull=True,
        subtopic__topic__subject__exam__name="LUMS",
        subtopic__topic__subject__name__in=["Math", "Verbal"],
    )

    to_deactivate = [
        q for q in candidates
        if (q.question_text, q.option_a) in paper_signatures
    ]
    print(f"Found {candidates.count()} standalone LUMS Math/Verbal practice rows, "
          f"{len(to_deactivate)} match the paper content exactly (duplicates).")

    for q in to_deactivate:
        print(f"  id={q.id}  active={q.is_active}  {q.question_text[:60]!r}")

    if opts.apply:
        ids = [q.id for q in to_deactivate]
        updated = Question.objects.filter(id__in=ids).update(is_active=False)
        print(f"Deactivated {updated} duplicate rows.")
    else:
        print("Dry run only — pass --apply to deactivate these rows.")


if __name__ == "__main__":
    main()
