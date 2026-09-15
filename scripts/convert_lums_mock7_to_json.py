"""Convert LCAT Mock 7 (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_mock_07.py -- a ParhaiKarlo-written
full-length 120-Q mock (7 sections, Verbal 69 / Math 51). Not an official
LUMS paper and no official answer key exists for it.

When first opened, this file's own docstring/SOURCE identified it as
"Mock Test #3" / "parhaikarlo_mock_03" -- the same filename-vs-content
mismatch class seen in Mocks 4, 5 and 6. Unlike the very first version
opened this session (which turned out to be 114/120 byte-identical to
Mock 5 -- a stale leftover copy under the wrong filename, never converted),
the content actually saved to lums_mock_07.py is genuinely new. Fixed the
header/SOURCE in the source file directly.

Same deliberate differences from convert_lums_sample_to_json.py as every
other LUMS mock converter:

  - needs_review is False, so import_mcqs.py lands every row with
    is_verified=True. Before conversion (2026-09-15) all 120 keys were
    checked: all 51 Math items (sections 2/4/6) were independently
    recomputed by script and matched the stated key (after fixing the
    items below); Verbal items were spot-checked for grammar/logic. That
    pass fixed one real defect -- Q79 used "its" for a plural-of-people
    antecedent ("date growers' export contract"), the SAME recurring error
    class as Q79 in every one of Mocks 3, 4, 5 and 6 -- now the confirmed
    standing weak point in this mock series' authoring process, worth
    checking first in any future mock before anything else.

    The source file's own check_other_bank_collisions() had the same
    latent bug every prior mock file shipped with (wrong module names,
    checking none of the real lums_mock_0N filenames). Fixed directly in
    the source file (now checks lums_mock_01 through lums_mock_06). Once
    fixed, it caught thirteen verbatim duplicates -- Q60 against Mock 1;
    Q25/Q32/Q33/Q58/Q92 against Mock 2; Q96 against Mock 3; Q34/Q69
    against Mock 4; Q105 against Mock 5 (an entire Craft-and-Structure
    passage reused verbatim); Q65/Q100 against Mock 6 -- all replaced with
    fresh, non-colliding items in the same topic/subtopic/difficulty/
    section and (mostly) the same answer letter. Several replacement
    attempts needed a second or third pass each, because the first
    replacement's numbers coincidentally matched a *different* mock's
    existing values (e.g. Q33's first retry at 100pi collided with Mock 3;
    Q100's first retry at an 11 cm short leg also collided with Mock 3) --
    always re-run the collision checker after every replacement, never
    assume one fix is final.

  - subtopic is the source file's real subtopic, not a copy of topic.

Topic tagging: skipped, as for every other LUMS bank. The source file's own
check_canonical_labels() asserts each topic/subtopic string already comes
from lums-content/syllabus/lums_syllabus.json.

paper_year stays None: this is a mock, not a dated paper. It attaches to a
quiz.MockTest row via scripts/attach_lums_mock7.py, so past_paper stays NULL
on every row.

Known non-blocking issue, not fixed: answer-letter balance is skewed
(A=40 B=38 C=25 D=17) -- the same skew pattern Mocks 2/3/6 originally
shipped with. Left as-is per this series' established precedent --
rebalancing would mean rewriting distractors on dozens of unrelated
questions, out of proportion to a single pass.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_mock_07 import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-mock-7-q{q['id']}",
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
            "source_file": "lums-content/raw-sources/lums_mock_07.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_7.json"
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
