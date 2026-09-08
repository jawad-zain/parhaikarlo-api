"""Convert the LUMS LCAT sample question bank (.py) into importer-ready JSON.

Source: lums-content/raw-sources/lums_lcat_sample.py — LUMS' own official
"Sample Questions for Verbal & Math Sections" guide, 24 Qs (Verbal 14, Math 10).

This is NOT a dated past paper (no official answer key exists for it — see the
docstring in the source file), so unlike the MDCAT_<YEAR>.json convention:
  - paper_year is None. It stays a standalone practice bank, not attached to
    any PastPaper row (mirrors mdcat-content's *_practice.py convention).
  - needs_review is forced True on every question regardless of topic-tag
    confidence, so import_mcqs.py lands every row with is_verified=False.
    Reasoning: the correct_answer values were reasoned out by whoever built
    the source file, not sourced from an official key, so nothing here earns
    is_verified=True until a human checks it against a released key.

Topic tagging: the source file already labels each question with its official
LUMS/digital-SAT-style domain (e.g. "Craft and Structure", "Advanced
Mathematics") straight from LUMS' own guide. That's already correct,
closed-vocabulary metadata — re-running it through the Groq tagger would only
risk *degrading* it. So this adapter skips tag_topics.py entirely and passes
the source topic straight through (tag_confidence="high"), the same shortcut
convert_english_practice_to_json.py and friends use for pre-tagged content.
Subtopic is set equal to topic (no finer breakdown exists yet in a 24-Q
sample) — real past papers, once ingested, can split these into proper
subtopics via lums_syllabus.json + the tagger as usual.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "lums-content" / "raw-sources"))

from lums_lcat_sample import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"lums-lcat-sample-q{q['id']}",
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
            "needs_review": True,  # no official key — force is_verified=False
            "source_file": "lums-content/raw-sources/lums_lcat_sample.py",
            "topic": q["topic"],
            "subtopic": q["topic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_LCAT_SAMPLE.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')

    subjects_seen = sorted({q['subject'] for q in out if q['subject']})
    print(f"Wrote {len(out)} MCQs to {out_path}")
    print(f"  with correct answer: {sum(1 for q in out if q['correct_answer'])}")
    print(f"  needs review (unverified, no official key): {sum(1 for q in out if q['needs_review'])}")
    print(f"  subjects: {subjects_seen}")
    print("\n  per-topic counts:")
    topics_seen = sorted({q['topic'] for q in out})
    for t in topics_seen:
        c = sum(1 for q in out if q['topic'] == t)
        print(f"    {t}: {c}")

    # dedupe / integrity checks
    ids = [q["id"] for q in out]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print(f"  WARNING duplicate ids: {dupes}")
    ans_letters = {}
    for q in out:
        ans_letters[q["correct_answer"]] = ans_letters.get(q["correct_answer"], 0) + 1
    print(f"  answer letter balance: {ans_letters}")


if __name__ == '__main__':
    main()
