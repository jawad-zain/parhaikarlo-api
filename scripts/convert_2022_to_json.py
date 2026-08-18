import json
import sys
from pathlib import Path

# Load the source .py as a module
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / 'mdcat-content'))
from mdcat_2022_source import SUBJECTS, QUESTIONS, KEY_RAW


def subject_for(qnum):
    for name, start, end in SUBJECTS:
        if start <= qnum <= end:
            return name.capitalize()  # matches Biology/Chemistry/... in your DB
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
        needs_review = subject is None or correct is None

        out.append({
            "id": f"mdcat-2022-q{qnum}",
            "paper_year": 2022,
            "question_number": qnum,
            "subject": subject,
            "question_text": text,
            "options": {"a": opts[0], "b": opts[1], "c": opts[2], "d": opts[3]},
            "correct_answer": correct,
            "difficulty": None,
            "explanation": None,
            "needs_review": needs_review,
            "source_file": "mdcat_2022_source.py",
        })

    out_path = ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_2022.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')

    print(f"Wrote {len(out)} MCQs to {out_path}")
    print(f"  with correct answer: {sum(1 for q in out if q['correct_answer'])}")
    print(f"  needs review: {sum(1 for q in out if q['needs_review'])}")
    print(f"  subjects: {sorted({q['subject'] for q in out if q['subject']})}")


if __name__ == '__main__':
    main()