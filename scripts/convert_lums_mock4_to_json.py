"""Convert LCAT Mock 4 (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_mock_04.py -- a ParhaiKarlo-written
full-length 120-Q mock (7 sections, Verbal 69 / Math 51). Not an official
LUMS paper and no official answer key exists for it.

Note on this file's history (2026-09-15): when first opened, this file's
docstring/SOURCE identified it as "Mock Test #3" and its content was 118/120
identical to lums_mock_03.py's pre-fix content -- it appears to have started
as a leftover copy of an earlier mock_03 draft. By the time the content
check below ran, the file had been rewritten with genuinely distinct
questions (confirmed via direct re-read after clearing __pycache__). Treat
this history as resolved; the content actually imported is the final,
distinct version checked in below.

Same two deliberate differences from convert_lums_sample_to_json.py as
every other LUMS mock converter:

  - needs_review is False, so import_mcqs.py lands every row with
    is_verified=True. Before conversion (2026-09-15) all 120 keys were
    checked: math items (51 of 51, sections 2/4/6) were independently
    recomputed and all matched the stated key; verbal items were spot-checked
    for grammar/logic. That pass fixed one real defect (Q79 used "its" for a
    plural-of-people antecedent -- "shopkeepers' electricity bill" -- where
    "their" is the only grammatical choice; same error class found and fixed
    in Mock 3's Q79). The source file's own check_other_bank_collisions()
    also had the same latent bug Mock 3's had -- it imported nonexistent
    modules ("lums_lcat_mock_01/02") instead of the real "lums_mock_01/02"
    filenames, and didn't check against Mock 3 at all; fixed directly in the
    source file (now checks lums_mock_01/02/03). Once fixed, it caught four
    verbatim duplicates against Mock 1 (Q101) and Mock 3 (Q26, Q58, Q100),
    all replaced with fresh, non-colliding items in the same
    topic/subtopic/difficulty/section (Q100's first replacement attempt
    coincidentally collided with Mock 2's own Q100 and needed a second
    replacement).

  - subtopic is the source file's real subtopic, not a copy of topic.

Topic tagging: skipped, as for every other LUMS bank. The source file's own
check_canonical_labels() asserts each topic/subtopic string already comes
from lums-content/syllabus/lums_syllabus.json.

paper_year stays None: this is a mock, not a dated paper. It attaches to a
quiz.MockTest row via scripts/attach_lums_mock4.py, so past_paper stays NULL
on every row.

Answer-letter balance for this bank came out clean on its own: A=31 B=30
C=29 D=30, close to even without any deliberate rebalancing needed (unlike
Mock 2's and Mock 3's skews).
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_mock_04 import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-mock-4-q{q['id']}",
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
            "source_file": "lums-content/raw-sources/lums_mock_04.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_4.json"
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
