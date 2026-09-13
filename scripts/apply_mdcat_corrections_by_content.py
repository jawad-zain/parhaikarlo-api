"""Apply MDCAT past-paper content corrections to a DB where PKs differ (prod).

Companion to the 2026-09-11 content+typography passes on MDCAT 2024 and 2025.
The corrections were applied to the local DB and to
mdcat-content/parsed-mcqs/MDCAT_<year>.json; this script carries the same
changes to another database by matching on the question's ORIGINAL
(question_text, option_a) rather than on id, exactly like
load_explanations_by_content does for explanations.

Safe by default: prints the full before/after diff and writes nothing unless
--apply is passed. Re-running after a successful run is a no-op (rows are
matched on their pre-fix text, which no longer exists once fixed).

Usage (from backend/, with the target DB configured in .env):
    py -3.14 scripts/apply_mdcat_corrections_by_content.py 2024 2025
    py -3.14 scripts/apply_mdcat_corrections_by_content.py 2024 2025 --apply
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

from django.db import transaction  # noqa: E402
from content.models import Question  # noqa: E402

FIELDS = ("question_text", "option_a", "option_b", "option_c", "option_d",
          "correct_answer")


def run(years, apply_changes):
    planned, missing, ambiguous, already, total = [], [], [], 0, 0

    for year in years:
        path = ROOT / "scripts" / f"mdcat_{year}_corrections_by_content.json"
        if not path.exists():
            print(f"no correction file for {year}: {path.name}")
            continue
        corrections = json.loads(path.read_text(encoding="utf-8"))
        total += len(corrections)
        print(f"\n=== MDCAT {year}: {len(corrections)} corrected questions ===")

        # A question fixed in several passes has one entry per pass, each keyed
        # on the text the previous pass left behind. Once a later pass has
        # applied, the earlier entry's post-fix text is gone too; it is still
        # "already applied" if a later entry picks up exactly where it ends.
        match_keys = {(c["match_question_text"], c["match_option_a"])
                      for c in corrections}

        for c in corrections:
            post_key = (c["set"].get("question_text", c["match_question_text"]),
                        c["set"].get("option_a", c["match_option_a"]))
            if post_key != (c["match_question_text"], c["match_option_a"]) \
                    and post_key in match_keys:
                if not Question.objects.filter(
                        past_paper__year=c["year"],
                        question_text=c["match_question_text"],
                        option_a=c["match_option_a"]).exists():
                    already += 1
                    continue
            qs = Question.objects.filter(
                past_paper__year=c["year"],
                question_text=c["match_question_text"],
                option_a=c["match_option_a"],
            )
            n = qs.count()
            if n == 0:
                # Already corrected? Look for the post-fix text instead.
                post = c["set"].get("question_text", c["match_question_text"])
                if Question.objects.filter(past_paper__year=c["year"],
                                           question_text=post).exists():
                    already += 1
                else:
                    missing.append((c["year"], c["question_number"]))
                continue
            if n > 1:
                ambiguous.append((c["year"], c["question_number"], n))
                continue
            q = qs.first()
            diff = {f: v for f, v in c["set"].items() if getattr(q, f) != v}
            if diff:
                planned.append((q, c, diff))
            else:
                already += 1

    print("\n" + "=" * 70)
    for q, c, diff in planned:
        print(f"\nMDCAT {c['year']} Q{c['question_number']} (target id {q.id})")
        for f, v in diff.items():
            print(f"  {f}\n    - {getattr(q, f)!r}\n    + {v!r}")

    print("\n" + "=" * 70)
    print(f"to change : {len(planned)} questions, "
          f"{sum(len(d) for _, _, d in planned)} fields")
    print(f"already ok: {already}")
    print(f"accounted : {len(planned) + already + len(missing) + len(ambiguous)} of {total}")
    if missing:
        print(f"NOT FOUND : {len(missing)} -> {missing}")
    if ambiguous:
        print(f"AMBIGUOUS : {len(ambiguous)} -> {ambiguous}")

    if not apply_changes:
        print("\nDRY RUN - nothing written. Re-run with --apply to save.")
        return
    if missing or ambiguous:
        print("\nRefusing to write while some questions are unmatched or "
              "ambiguous. Resolve those first.")
        return

    with transaction.atomic():
        for q, _c, diff in planned:
            for f, v in diff.items():
                setattr(q, f, v)
            q.save(update_fields=list(diff))
    print(f"\nAPPLIED to {len(planned)} questions.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    run(args or ["2024", "2025"], "--apply" in sys.argv)
