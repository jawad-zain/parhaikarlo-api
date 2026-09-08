"""DB-wide collision check: does any (question_text, option_a) pair in
MDCAT_MOCK_18.json already exist among Question rows with
past_paper=NULL (the exact dedupe key import_mcqs.py uses)? This
catches legacy/deactivated rows that may not appear in any current
parsed-mcqs JSON file (see the Q112 vs old-mock_1 stale-row incident).
Checks ALL rows including is_active=False.
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

data = json.loads((ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_MOCK_18.json").read_text(encoding="utf-8"))

collisions = []
exact_dup = []
for mcq in data:
    matches = Question.objects.filter(
        past_paper__isnull=True,
        question_text=mcq["question_text"],
        option_a=mcq["options"]["a"],
    )
    for m in matches:
        rec = (mcq["question_number"], m.id, m.is_active, m.option_b, mcq["options"]["b"])
        if m.option_b != mcq["options"]["b"]:
            collisions.append(rec)
        else:
            exact_dup.append(rec)

print(f"Checked {len(data)} questions against live DB (including inactive rows)")
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
