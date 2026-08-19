"""
Adapter: mdcat_2013.py -> parsed-mcqs/MDCAT_2013.json

Differences from the 2014 adapter:
- This file currently covers questions 1-112 only (first half of the 220-question
  paper); the rest will be appended in a follow-up pass and this script can be
  re-run safely (import_mcqs upserts on (paper, question_text, option_a)).
- KEY_RAW is complete (no UNRESOLVED entries) -- every question has a real answer.
- DIAGRAM_MCQS here is informational only (editorial notes on which questions
  need a figure). It does NOT force is_active=False / needs_review=True, because
  real cropped images get attached to these questions via import_question_images
  right after this import, instead of leaving them inactive placeholders.
"""
import json
import importlib.util
from pathlib import Path

# --- paths ---
SOURCE_FILE = Path("mdcat-content/mdcat_2013.py")
OUTPUT_FILE = Path("mdcat-content/parsed-mcqs/MDCAT_2013.json")
PAPER_YEAR = 2013

# --- load the .py source as a module ---
spec = importlib.util.spec_from_file_location("mdcat_2013", SOURCE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

SUBJECTS = mod.SUBJECTS          # [(name, start, end), ...]
QUESTIONS = mod.QUESTIONS        # {n: (text, [opts])}
KEY_RAW = mod.KEY_RAW            # "N letter\nN letter\n..."
DIAGRAM_MCQS = getattr(mod, "DIAGRAM_MCQS", {})


def subject_for(qnum: int) -> str:
    for name, start, end in SUBJECTS:
        if start <= qnum <= end:
            return name.capitalize()   # BIOLOGY -> Biology
    raise ValueError(f"Q{qnum} outside any SUBJECTS range")


def parse_key(raw: str) -> dict:
    key = {}
    for line in raw.strip().splitlines():
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        qnum_str, letter = parts
        qnum = int(qnum_str)
        letter = letter.strip().lower()
        if letter in {"a", "b", "c", "d"}:
            key[qnum] = letter
        else:
            key[qnum] = None
    return key


ANSWER_KEY = parse_key(KEY_RAW)

out = []
stats = {"total": 0, "diagram_needs_image": 0, "inactive_unresolved": 0, "active": 0}

for qnum in sorted(QUESTIONS.keys()):
    text, opts = QUESTIONS[qnum]
    if len(opts) != 4:
        print(f"WARN Q{qnum}: expected 4 options, got {len(opts)} -- skipping")
        continue

    answer = ANSWER_KEY.get(qnum)
    diagram_note = DIAGRAM_MCQS.get(qnum)

    is_active = True
    needs_review = False
    notes = None

    if diagram_note:
        notes = diagram_note.get("note")
        needs_review = True   # stays flagged for human review until the image is attached
        stats["diagram_needs_image"] += 1

    if answer is None:
        is_active = False
        needs_review = True
        notes = f"Answer key entry for Q{qnum} unresolved in source -- verify against original key image"
        stats["inactive_unresolved"] += 1
    else:
        stats["active"] += 1

    out.append({
        "id": f"mdcat-{PAPER_YEAR}-q{qnum}",
        "paper_year": PAPER_YEAR,
        "question_number": qnum,
        "subject": subject_for(qnum),
        "topic": None,
        "subtopic": None,
        "difficulty": None,
        "question_text": text,
        "options": {"a": opts[0], "b": opts[1], "c": opts[2], "d": opts[3]},
        "correct_answer": answer,
        "explanation": None,
        "is_active": is_active,
        "needs_review": needs_review,
        "notes": notes,
        "source_file": SOURCE_FILE.name,
    })
    stats["total"] += 1

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"\nWrote {len(out)} MCQs to {OUTPUT_FILE}")
print(f"  active: {stats['active']}")
print(f"  diagram (needs image attached): {stats['diagram_needs_image']}")
print(f"  inactive (unresolved key): {stats['inactive_unresolved']}")
