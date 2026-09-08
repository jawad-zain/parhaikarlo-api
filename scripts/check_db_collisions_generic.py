"""Generic DB-wide collision check: does any (question_text, option_a) pair
in a given parsed-mcqs JSON file already exist among Question rows with
past_paper=NULL (the exact dedupe key import_mcqs.py uses)? Checks ALL rows
including is_active=False, so it also catches legacy/deactivated rows.

Usage (from backend/, venv active):
    python scripts/check_db_collisions_generic.py <path/to/parsed.json>
"""
import json
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question

json_path = Path(sys.argv[1])
data = json.loads(json_path.read_text(encoding="utf-8"))

collisions = []
exact_dup = []
for mcq in data:
    matches = Question.objects.filter(
        past_paper__isnull=True,
        question_text=mcq["question_text"],
        option_a=mcq["options"]["a"],
    )
    for m in matches:
        rec = (mcq.get("question_number"), m.id, m.is_active, m.option_b, mcq["options"]["b"])
        if m.option_b != mcq["options"]["b"]:
            collisions.append(rec)
        else:
            exact_dup.append(rec)

print(f"Checked {len(data)} questions from {json_path.name} against live DB (including inactive rows)")
if collisions:
    print(f"COLLISIONS FOUND (option_b differs -> would corrupt on import_mcqs update): {len(collisions)}")
    for c in collisions:
        print(" ", c)
else:
    print("No DB collisions found (option_b differs).")

if exact_dup:
    print(f"EXACT DUPLICATE ROWS (identical text+a+b, likely a true re-import): {len(exact_dup)}")
    for c in exact_dup:
        print(" ", c)
else:
    print("No exact-duplicate rows found.")
