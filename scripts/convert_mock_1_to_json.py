import json
import sys
from pathlib import Path

# Load the source .py as a module
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / 'mdcat-content'))
from mdcat_mock_1 import SUBJECTS, QUESTIONS, KEY_RAW, TOPIC_TAGS, VISUAL_MCQS


def subject_for(qnum):
    for name, start, end in SUBJECTS:
        if start <= qnum <= end:
            return name.capitalize() if name != "LOGICAL REASONING" else "Logical Reasoning"
    return None


def parse_key(raw):
    """KEY_RAW is 'Q ans Q ans ...' whitespace-separated. Flatten to {qnum: letter}."""
    tokens = raw.split()
    key = {}
    i = 0
    while i < len(tokens) - 1:
        try:
            q = int(tokens[i])
            ans = tokens[i + 1].lower()
            if ans in {'a', 'b', 'c', 'd'}:
                key[q] = ans
                i += 2
            else:
                i += 1
        except ValueError:
            i += 1
    return key


def main():
    key = parse_key(KEY_RAW)
    out = []

    for qnum in sorted(QUESTIONS.keys()):
        text, opts = QUESTIONS[qnum]
        subject = subject_for(qnum)
        correct = key.get(qnum)
        tag = TOPIC_TAGS.get(qnum)
        topic, subtopic, difficulty = tag if tag else (None, None, None)
        is_visual = qnum in VISUAL_MCQS
        needs_review = subject is None or correct is None or topic is None or is_visual

        out.append({
            "id": f"mdcat-mock1-q{qnum}",
            "paper_year": None,          # not tied to a real past paper/year
            "mock_test": "MDCAT Mock Test 1",
            "question_number": qnum,
            "subject": subject,
            "question_text": text,
            "options": {"a": opts[0], "b": opts[1], "c": opts[2], "d": opts[3]},
            "correct_answer": correct,
            "difficulty": difficulty,
            "explanation": None,
            "needs_review": needs_review,
            "source_file": "mdcat_mock_1.py",
            "topic": topic,
            "subtopic": subtopic,
            "tag_confidence": "high",
            "is_visual_required": is_visual,
        })

    out_path = ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_MOCK_1.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')

    subjects_seen = sorted({q['subject'] for q in out if q['subject']})
    print(f"Wrote {len(out)} MCQs to {out_path}")
    print(f"  with correct answer: {sum(1 for q in out if q['correct_answer'])}")
    print(f"  needs review: {sum(1 for q in out if q['needs_review'])}")
    print(f"  visual/image questions: {sum(1 for q in out if q['is_visual_required'])}")
    print(f"  subjects: {subjects_seen}")
    print("\n  per-subject counts and % of 200:")
    for s in subjects_seen:
        c = sum(1 for q in out if q['subject'] == s)
        print(f"    {s}: {c}  ({c/len(out)*100:.1f}%)")


if __name__ == '__main__':
    main()
