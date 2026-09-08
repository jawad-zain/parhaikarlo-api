"""DB-wide collision check: does any (question_text, option_a) pair in
MDCAT_MOCK_17.json already exist among Question rows with
past_paper=NULL (the exact dedupe key import_mcqs.py uses)? This
catches legacy/deactivated rows that may not appear in any current
parsed-mcqs JSON file (see the Q112 vs old-mock_1 stale-row incident).
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

data = json.loads((ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_MOCK_17.json").read_text(encoding="utf-8"))

collisions = []
for mcq in data:
    any_match = Question.objects.filter(
        past_paper__isnull=True,
        question_text=mcq["question_text"],
        option_a=mcq["options"]["a"],
    ).first()
    if any_match and any_match.option_b != mcq["options"]["b"]:
        collisions.append((mcq["question_number"], any_match.id, any_match.option_b, mcq["options"]["b"]))

print(f"Checked {len(data)} questions against live DB")
if collisions:
    print(f"COLLISIONS FOUND: {len(collisions)}")
    for c in collisions:
        print(" ", c)
else:
    print("No DB collisions found.")
