"""Convert LCAT Mock 8 (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_mock_08.py -- a ParhaiKarlo-written
full-length 120-Q mock (7 sections, Verbal 69 / Math 51). Not an official
LUMS paper and no official answer key exists for it.

When first opened, this file's own docstring/SOURCE identified it as
"Mock Test #5" / "parhaikarlo_mock_05" -- the same filename-vs-content
mismatch class seen in Mocks 4, 5 and 6. Diffing its (question_text,
option_a) pairs against every prior bank found only a handful of scattered
coincidental overlaps (not a contiguous block), so -- like Mock 5's own
precedent -- this was treated as a harmless label bug, not a stale copy.
Fixed the header/SOURCE in the source file directly.

Same deliberate differences from convert_lums_sample_to_json.py as every
other LUMS mock converter:

  - needs_review is False, so import_mcqs.py lands every row with
    is_verified=True. Before conversion (2026-09-15) all 120 keys were
    checked: all 51 Math items (sections 2/4/6) were independently
    recomputed by hand and matched the stated key (after fixing the items
    below); every Verbal item was checked for grammar/logic. That pass
    fixed two real defects -- Q79 used "its" for a plural-of-people
    antecedent ("surveyed shopkeepers' electricity bill"), the SAME
    recurring error class as Q79 in every one of Mocks 3-7; and Q11 had
    the mirror-image error -- "their" used for a singular organisational
    antecedent ("the dockworkers' union[...] objection"), where Standard
    English calls for the singular "its". Both fixed in the source file.

    The source file's own check_other_bank_collisions() had the same
    latent bug every prior mock file shipped with (wrong module names,
    checking none of the real lums_mock_0N filenames, and missing Mocks
    5-7 entirely). Fixed directly in the source file (now checks
    lums_mock_01 through lums_mock_07). Once fixed, it caught ten verbatim
    duplicates -- Q33 against Mock 6; Q51/Q58/Q65/Q94/Q97 against Mock 5;
    Q60/Q99/Q100 against Mock 4; Q85 against Mock 7 -- all replaced with
    fresh, non-colliding items in the same topic/subtopic/difficulty/
    section and same answer letter. Three of the ten replacements (Q51,
    Q58, Q65) needed a second attempt after colliding with a *different*
    mock on retry, and Q51/Q65 needed a third attempt after that -- always
    re-run the collision checker after every replacement, never assume one
    fix is final.

  - subtopic is the source file's real subtopic, not a copy of topic.

Topic tagging: skipped, as for every other LUMS bank. The source file's own
check_canonical_labels() asserts each topic/subtopic string already comes
from lums-content/syllabus/lums_syllabus.json.

paper_year stays None: this is a mock, not a dated paper. It attaches to a
quiz.MockTest row via scripts/attach_lums_mock8.py, so past_paper stays NULL
on every row.

Answer-letter balance after fixes: A=32 B=42 C=29 D=17 -- skewed toward B
and away from D, the same pattern seen in several prior mocks in this
series, but not as extreme as Mock 2's original 61/120 B-skew that
triggered a deliberate rebalancing pass. Left as-is per this series'
established precedent (Mocks 3, 6 and 7 also left comparable skews alone).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_mock_08 import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-mock-8-q{q['id']}",
            "paper_year": None,
            "question_number": q["id"],
            "subject": q["subject"],
            "question_text": q["question"],
            "options": {
                "a": q["options"]["A"],
                "b": q["options"]["B"],
                "c": q["options"]["C"],
                "d": q["options"]["D"],
            },
            "correct_answer": q["answer"].lower(),
            "difficulty": q["difficulty"].lower(),
            "explanation": None,
            "needs_review": False,  # keys content-verified 2026-09-15
            "source_file": "lums-content/raw-sources/lums_mock_08.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_8.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Wrote {len(out)} MCQs to {out_path}")
    print(f"  with correct answer: {sum(1 for q in out if q['correct_answer'])}")
    print(f"  needs review: {sum(1 for q in out if q['needs_review'])}")

    subjects_seen = sorted({q["subject"] for q in out if q["subject"]})
    for s in subjects_seen:
        print(f"  subject {s}: {sum(1 for q in out if q['subject'] == s)}")

    ans_letters = {}
    for q in out:
        ans_letters[q["correct_answer"]] = ans_letters.get(q["correct_answer"], 0) + 1
    print(f"  answer letter balance: {dict(sorted(ans_letters.items()))}")

    ids = [q["id"] for q in out]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print(f"  WARNING duplicate ids: {dupes}")

    pairs = [(q["question_text"], q["options"]["a"]) for q in out]
    if len(set(pairs)) != len(pairs):
        print("  WARNING duplicate (question_text, option_a) pairs within this bank")


if __name__ == "__main__":
    main()
