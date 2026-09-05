import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "mdcat-content"))

from mdcat_logica_reasoning_practice import QUESTIONS  # noqa: E402


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"mdcat-logical-reasoning-practice-q{q['id']}",
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
            "needs_review": False,
            "source_file": "mdcat_logica_reasoning_practice.py",
            "topic": q["topic"],
            "subtopic": q["subtopic"],
            "tag_confidence": "high",
            "is_visual_required": False,
            "image": None,
        })

    out_path = ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_LOGICAL_REASONING_PRACTICE.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')

    subjects_seen = sorted({q['subject'] for q in out if q['subject']})
    print(f"Wrote {len(out)} MCQs to {out_path}")
    print(f"  with correct answer: {sum(1 for q in out if q['correct_answer'])}")
    print(f"  needs review: {sum(1 for q in out if q['needs_review'])}")
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
