"""Check (question_text, option_a) collisions between MDCAT_MOCK_16.json
and every other parsed-mcqs JSON (past papers + Mocks 1-14)."""
import json
from pathlib import Path

DIR = Path(__file__).parent.parent / "mdcat-content" / "parsed-mcqs"
TARGET = DIR / "MDCAT_MOCK_16.json"

target = json.loads(TARGET.read_text(encoding="utf-8"))
target_keys = {(q["question_text"], q["options"]["a"]): q["question_number"] for q in target}

other_files = sorted(
    p for p in DIR.glob("MDCAT_*.json")
    if p.name != "MDCAT_MOCK_16.json" and p.suffix == ".json" and "checkpoint" not in p.name
)

collisions = []
for p in other_files:
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"skip {p.name}: {e}")
        continue
    if not isinstance(data, list):
        continue
    for q in data:
        if not isinstance(q, dict) or "question_text" not in q or "options" not in q:
            continue
        key = (q.get("question_text"), q.get("options", {}).get("a"))
        if key in target_keys:
            collisions.append((p.name, q.get("question_number"), target_keys[key]))

print(f"Checked against {len(other_files)} files")
if collisions:
    print(f"COLLISIONS FOUND: {len(collisions)}")
    for c in collisions:
        print(" ", c)
else:
    print("No collisions found.")
