"""Convert LCAT Mock 5 (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_mock_05.py -- a ParhaiKarlo-written
full-length 120-Q mock (7 sections, Verbal 69 / Math 51). Not an official
LUMS paper and no official answer key exists for it.

Same "docstring/SOURCE mismatched with filename" signal seen in Mock 4 was
present here too (this file's own header called itself "Mock Test #4" /
"parhaikarlo_mock_04"), but unlike Mock 4, direct diffing against every
prior bank showed only a handful (6) of small, coincidental numeric-template
overlaps, not wholesale duplication -- treated as the same defect class the
collision checker below exists to catch, not a sign the file needed
rewriting.

Same deliberate differences from convert_lums_sample_to_json.py as every
other LUMS mock converter:

  - needs_review is False, so import_mcqs.py lands every row with
    is_verified=True. Before conversion (2026-09-15) all 120 keys were
    checked: math items (51 of 51, sections 2/4/6) were independently
    recomputed and all matched the stated key; verbal items were spot-checked
    for grammar/logic. That pass fixed one real defect (Q79 used "its" for a
    plural-of-people antecedent -- "orchard owners' irrigation allocation" --
    the same recurring error class already found and fixed in Mock 3's and
    Mock 4's own Q79). The source file's own check_other_bank_collisions()
    had the same latent bug every prior mock file shipped with (wrong module
    names, "lums_lcat_mock_01/02/03", and no check against Mock 4 at all);
    fixed directly in the source file (now checks lums_mock_01/02/03/04).
    Once fixed, it caught six verbatim duplicates -- Q26/Q66 against Mock 1,
    Q101 against Mock 2, Q53/Q69/Q97 against Mock 3 -- all replaced with
    fresh, non-colliding items in the same
    topic/subtopic/difficulty/section, same answer letter (so the bank's
    already-even A/B/C/D balance barely moved).

  - subtopic is the source file's real subtopic, not a copy of topic.

Topic tagging: skipped, as for every other LUMS bank. The source file's own
check_canonical_labels() asserts each topic/subtopic string already comes
from lums-content/syllabus/lums_syllabus.json.

paper_year stays None: this is a mock, not a dated paper. It attaches to a
quiz.MockTest row via scripts/attach_lums_mock5.py, so past_paper stays NULL
on every row.

Answer-letter balance: A=31 B=30 C=29 D=30 after the Q79 fix flipped one
question from C to A -- close to even, no deliberate rebalancing needed.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_mock_05 import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-mock-5-q{q['id']}",
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
            "source_file": "lums-content/raw-sources/lums_mock_05.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_5.json"
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
