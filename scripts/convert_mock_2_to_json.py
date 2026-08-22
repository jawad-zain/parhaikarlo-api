import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / 'mdcat-content'))
from mdcat_mock_2 import QUESTIONS


def main():
    out = []

    for q in QUESTIONS:
        out.append({
            "id": f"mdcat-mock2-q{q['id']}",
            "paper_year": None,
            "mock_test": "MDCAT Mock Test 2",
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
            "source_file": "mdcat_mock_2.py",
            "topic": q["topic"],
            "subtopic": q["topic"],
            "tag_confidence": "high",
            "is_visual_required": "image" in q,
            "image": q.get("image"),
        })

    out_path = ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_MOCK_2.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')

    subjects_seen = sorted({q['subject'] for q in out if q['subject']})
    print(f"Wrote {len(out)} MCQs to {out_path}")
    print(f"  with correct answer: {sum(1 for q in out if q['correct_answer'])}")
    print(f"  needs review: {sum(1 for q in out if q['needs_review'])}")
    print(f"  visual/image questions: {sum(1 for q in out if q['is_visual_required'])}")
    print(f"  subjects: {subjects_seen}")
    print("\n  per-subject counts and % of total:")
    for s in subjects_seen:
        c = sum(1 for q in out if q['subject'] == s)
        print(f"    {s}: {c}  ({c/len(out)*100:.1f}%)")


if __name__ == '__main__':
    main()
