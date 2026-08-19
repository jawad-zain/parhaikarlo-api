"""
Adapter: mdcat_2012.py -> parsed-mcqs/MDCAT_2012.json

Same shape as convert_2013_to_json.py, with one addition: mdcat_2012.py has
14 questions whose options are unusable as-is (OCR-corrupted formulas, or
figure-only / lost-segment placeholders) -- see the CLEANUP PASS comments at
the top and bottom of mdcat_2012.py. Those questions have DIAGRAM_PLACEHOLDER
appended to their question_text; this script treats that marker as a hard
"deactivate until a human/source fixes it" signal (is_active=False), unlike
plain DIAGRAM_MCQS entries (which only need an image attached later and stay
active, per the 2013 adapter's convention).
"""
import json
import importlib.util
from pathlib import Path

# --- paths ---
SOURCE_FILE = Path("mdcat-content/mdcat_2012.py")
OUTPUT_FILE = Path("mdcat-content/parsed-mcqs/MDCAT_2012.json")
PAPER_YEAR = 2012

# --- load the .py source as a module ---
spec = importlib.util.spec_from_file_location("mdcat_2012", SOURCE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

SUBJECTS = mod.SUBJECTS          # [(name, start, end), ...]
QUESTIONS = mod.QUESTIONS        # {n: (text, [opts])}
KEY_RAW = mod.KEY_RAW            # "N letter\nN letter\n..."
DIAGRAM_MCQS = getattr(mod, "DIAGRAM_MCQS", {})
DIAGRAM_PLACEHOLDER = getattr(mod, "DIAGRAM_PLACEHOLDER", None)
SPOT_THE_ERROR_UNRESOLVED = getattr(mod, "SPOT_THE_ERROR_UNRESOLVED", set())


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
stats = {"total": 0, "diagram_needs_image": 0, "unresolved_blocked": 0, "inactive_unresolved_key": 0, "active": 0}

for qnum in sorted(QUESTIONS.keys()):
    text, opts = QUESTIONS[qnum]
    if len(opts) != 4:
        print(f"WARN Q{qnum}: expected 4 options, got {len(opts)} -- skipping")
        continue

    answer = ANSWER_KEY.get(qnum)
    diagram_note = DIAGRAM_MCQS.get(qnum)
    is_blocked = bool(DIAGRAM_PLACEHOLDER) and DIAGRAM_PLACEHOLDER in text

    is_active = True
    needs_review = False
    notes = None

    if diagram_note:
        notes = diagram_note.get("notes") or diagram_note.get("note")
        needs_review = True
        stats["diagram_needs_image"] += 1

    if is_blocked:
        is_active = False
        needs_review = True
        if qnum in SPOT_THE_ERROR_UNRESOLVED:
            notes = ("SPOT THE ERROR item: underlined-segment options lost to OCR, "
                     "not recoverable from this source. Needs the original 2012 PDF page.")
        else:
            notes = notes or "Options unresolved (OCR-corrupted / figure-only). Needs the original 2012 PDF page."
        stats["unresolved_blocked"] += 1

    if answer is None:
        is_active = False
        needs_review = True
        notes = f"Answer key entry for Q{qnum} unresolved in source (printed as 'x') -- verify against original key image"
        stats["inactive_unresolved_key"] += 1

    if is_active:
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
print(f"  diagram (needs image attached, still active): {stats['diagram_needs_image']}")
print(f"  unresolved/blocked (inactive): {stats['unresolved_blocked']}")
print(f"  inactive (unresolved key): {stats['inactive_unresolved_key']}")
