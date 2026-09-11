"""Convert LCAT Mock 1 (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_mock_01.py — a ParhaiKarlo-written
full-length 120-Q mock (7 sections, Verbal 69 / Math 51). Not an official
LUMS paper and no official answer key exists for it.

Same two deliberate differences from convert_lums_sample_to_json.py that
convert_lums_mock2_to_json.py documents:

  - needs_review is False, so import_mcqs.py lands every row with
    is_verified=True. The source file's own docstring still says
    NEEDS_REVIEW=True ("answer keys prepared by content team, pending human
    verification"), but that verification has since happened: every one of
    the 120 keys was cross-checked against the "Correct"/"Wrong" per-option
    labels in scripts/lums_mock1_explanations_by_content.json, which was
    authored independently of the key. All 120 agree, each question carries
    exactly one option labelled Correct, and the letter balance is already
    even (A 30 / B 29 / C 31 / D 30) — so this bank needed none of the
    rebalancing Mock 2 did. Unverified questions are invisible to
    /api/quiz/questions/, so leaving the flag on would import the mock and
    then hide it.

  - subtopic is the source file's real subtopic, not a copy of topic. The
    24-Q sample had no finer breakdown so it set subtopic = topic; this bank
    carries genuine subtopic labels ("Words in Context (vocabulary-in-blank)"
    under "Craft and Structure", and so on).

Topic tagging: skipped, as for every other LUMS bank. The source file's own
check_canonical_labels() asserts each topic/subtopic string already comes
from lums-content/syllabus/lums_syllabus.json, so running the Groq tagger
could only degrade correct closed-vocabulary labels.

paper_year stays None: this is a mock, not a dated paper. It attaches to a
quiz.MockTest row via scripts/attach_lums_mock1.py (the same home MDCAT
mocks use), so past_paper stays NULL on every row.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_mock_01 import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-mock-1-q{q['id']}",
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
            "needs_review": False,  # keys cross-checked against explanations 2026-09-12
            "source_file": "lums-content/raw-sources/lums_mock_01.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_1.json"
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
