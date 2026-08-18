"""
Adapter: mdcat_2014.py → parsed-mcqs/2014.json

Differences from 2022 adapter:
- SUBJECTS is list of (name, start, end) tuples (not plain list)
- QUESTIONS values are (text, options) 2-tuples (answer comes from KEY_RAW)
- KEY_RAW may contain 'UNRESOLVED' for OCR-artifact keys → import as inactive
- DIAGRAM_MCQS dict overrides is_active/needs_review/notes for diagram Qs
"""
import json
import importlib.util
from pathlib import Path

# --- paths ---
SOURCE_FILE = Path("mdcat-content/mdcat_2014.py")
OUTPUT_FILE = Path("mdcat-content/parsed-mcqs/MDCAT_2014.json")
PAPER_YEAR = 2014

# --- load the .py source as a module ---
spec = importlib.util.spec_from_file_location("mdcat_2014", SOURCE_FILE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

SUBJECTS = mod.SUBJECTS          # [(name, start, end), ...]
QUESTIONS = mod.QUESTIONS        # {n: (text, [opts])}
KEY_RAW = mod.KEY_RAW            # "N letter\nN letter\n..."
DIAGRAM_MCQS = getattr(mod, "DIAGRAM_MCQS", {})

# --- build qnum → subject map from tuple ranges ---
def subject_for(qnum: int) -> str:
    for name, start, end in SUBJECTS:
        if start <= qnum <= end:
            return name.capitalize()   # BIOLOGY → Biology
    raise ValueError(f"Q{qnum} outside any SUBJECTS range")

# --- parse KEY_RAW into {qnum: letter_or_None} ---
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
            key[qnum] = None   # 'UNRESOLVED', 'S', etc.
    return key

ANSWER_KEY = parse_key(KEY_RAW)

# --- convert ---
out = []
stats = {"total": 0, "inactive_diagram": 0, "inactive_unresolved": 0, "active": 0}

for qnum in sorted(QUESTIONS.keys()):
    text, opts = QUESTIONS[qnum]
    if len(opts) != 4:
        # diagram placeholder Qs use [PLACEHOLDER]*4, already length 4
        # anything else = malformed
        print(f"WARN Q{qnum}: expected 4 options, got {len(opts)} — skipping")
        continue

    answer = ANSWER_KEY.get(qnum)
    diagram_override = DIAGRAM_MCQS.get(qnum)

    # default flags
    is_active = True
    needs_review = False
    notes = None

    # diagram override wins
    if diagram_override:
        is_active = diagram_override.get("is_active", False)
        needs_review = diagram_override.get("needs_review", True)
        notes = diagram_override.get("notes")
        stats["inactive_diagram"] += 1

    # unresolved key (Q188 class)
    elif answer is None:
        is_active = False
        needs_review = True
        notes = f"Answer key entry for Q{qnum} unresolved in source — verify against original key image"
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

# --- write ---
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"\n✓ Wrote {len(out)} MCQs to {OUTPUT_FILE}")
print(f"  active: {stats['active']}")
print(f"  inactive (diagram): {stats['inactive_diagram']}")
print(f"  inactive (unresolved key): {stats['inactive_unresolved']}")