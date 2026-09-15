"""Convert LCAT Mock 6 (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_mock_06.py -- a ParhaiKarlo-written
full-length 120-Q mock (7 sections, Verbal 69 / Math 51). Not an official
LUMS paper and no official answer key exists for it.

Same docstring/SOURCE-vs-filename mismatch seen in Mocks 4 and 5 was present
here too (this file's own header called itself "Mock Test #2" /
"parhaikarlo_mock_02", and its collision-check function didn't even attempt
to import a mock_02 module, wrong-named or otherwise). Diffing against every
prior bank found 13/120 verbatim overlaps (elevated vs. Mocks 4/5's ~5-6,
but not wholesale duplication), all replaced -- see below.

Same deliberate differences from convert_lums_sample_to_json.py as every
other LUMS mock converter:

  - needs_review is False, so import_mcqs.py lands every row with
    is_verified=True. Before conversion (2026-09-15) all 120 keys were
    checked: math items (51 of 51, sections 2/4/6) were independently
    recomputed and all matched the stated key; verbal items were spot-checked
    for grammar/logic. That pass fixed one real defect (Q79 used "its" for a
    plural-of-people antecedent -- "cotton farmers' water allocation" -- the
    SAME recurring error class as Q79 in Mocks 3, 4, and 5; this pronoun
    slot is a confirmed standing weak point in this mock series' authoring
    process, worth checking first in any future mock). The source file's own
    check_other_bank_collisions() had the same latent bug every prior mock
    file shipped with (wrong module names, no check against 2-3 of the
    other mocks); fixed directly in the source file (now checks
    lums_mock_01 through lums_mock_05). Once fixed, it caught thirteen
    verbatim duplicates -- Q35 against Mock 1; Q17/Q30/Q61/Q66/Q69/Q91/Q95
    against Mock 2; Q33/Q53/Q65/Q85/Q97 against Mock 4 -- all replaced with
    fresh, non-colliding items in the same topic/subtopic/difficulty/
    section and (mostly) the same answer letter. Two replacement attempts
    (Q17, Q65) needed a SECOND pass each: the first replacement for each
    coincidentally collided with a different bank (Q17 first collided
    within this same file's own Q51 "PRUDENT" synonym question; the
    DILIGENT retry then collided with Mock 5's Q118; Q65's first retry at
    343 cm^3 collided with Mock 2's own Q65) -- always re-run the collision
    checker after every replacement, not just once.

  - subtopic is the source file's real subtopic, not a copy of topic.

Topic tagging: skipped, as for every other LUMS bank. The source file's own
check_canonical_labels() asserts each topic/subtopic string already comes
from lums-content/syllabus/lums_syllabus.json.

paper_year stays None: this is a mock, not a dated paper. It attaches to a
quiz.MockTest row via scripts/attach_lums_mock6.py, so past_paper stays NULL
on every row.

Known non-blocking issue, not fixed: answer-letter balance is skewed
(A=36 B=37 C=30 D=17) -- same pattern as Mock 2/3's original skew. Left
as-is per this series' established precedent (see Mock 2/3 README notes) --
rebalancing would mean rewriting distractors on dozens of unrelated
questions, out of proportion to a single pass. Flag for a future dedicated
rebalancing pass across the whole mock series if it matters for exam
realism.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_mock_06 import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-mock-6-q{q['id']}",
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
            "source_file": "lums-content/raw-sources/lums_mock_06.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_6.json"
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
