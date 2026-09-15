"""Convert LCAT Mock 3 (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_mock_03.py -- a ParhaiKarlo-written
full-length 120-Q mock (7 sections, Verbal 69 / Math 51). Not an official
LUMS paper and no official answer key exists for it.

Same two deliberate differences from convert_lums_sample_to_json.py as
convert_lums_mock2_to_json.py:

  - needs_review is False, so import_mcqs.py lands every row with
    is_verified=True. Before conversion (2026-09-15) all 120 keys were
    checked: math items (51 of 51, sections 2/4/6) were independently
    recomputed and all matched the stated key; verbal items were spot-checked
    for grammar/logic. That pass fixed one real defect (Q79 used "its" for a
    plural-of-people antecedent -- "vendors' stall rent" -- where "their"
    is the only grammatical singular-they choice; "its" is for inanimate
    referents) and two content bugs surfaced by the source file's own
    check_other_bank_collisions(): Q63 and Q68 were verbatim duplicates of
    Mock 1 Q63 and Mock 2 Q68 respectively (import_mcqs.py's
    (past_paper, question_text, option_a) dedupe key would have silently
    merged them into the wrong mock's question, since past_paper is NULL for
    every mock). Both were replaced with fresh, non-colliding items in the
    same topic/subtopic/difficulty/section. The source file's own
    check_other_bank_collisions() also had a latent bug of its own -- it
    imported nonexistent modules "lums_lcat_mock_01/02/03" instead of the
    real "lums_mock_01/02" filenames, so the Mock 1/2 collision checks had
    been silently no-op-ing; fixed in the source file directly.

  - subtopic is the source file's real subtopic, not a copy of topic.

Topic tagging: skipped, as for every other LUMS bank. The source file's own
check_canonical_labels() asserts each topic/subtopic string already comes
from lums-content/syllabus/lums_syllabus.json.

paper_year stays None: this is a mock, not a dated paper. It attaches to a
quiz.MockTest row via scripts/attach_lums_mock3.py, so past_paper stays NULL
on every row.

Known non-blocking issue (not fixed here, same as Mock 2's history): the
answer-letter balance is skewed (A=28 B=43 C=30 D=19 as of this conversion)
rather than an even ~30/30/30/30. Left as-is -- rebalancing would mean
rewriting distractors on dozens of unrelated questions, out of proportion to
this pass's scope. Flag for a future dedicated rebalancing pass.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_mock_03 import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-mock-3-q{q['id']}",
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
            "source_file": "lums-content/raw-sources/lums_mock_03.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_3.json"
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
