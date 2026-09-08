import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
dump = {q["id"]: q for q in json.load(open(ROOT / "mock17_db_dump.json", encoding="utf-8"))}

batch_file = sys.argv[1]
batch = json.load(open(batch_file, encoding="utf-8"))

mismatches = []
missing = []
for entry in batch:
    qid = entry["id"]
    if qid not in dump:
        missing.append(qid)
        continue
    correct_letter = dump[qid]["correct_answer"].lower()
    opts = entry["options"]
    marked_correct = [k for k, v in opts.items() if v.strip().lower().startswith("correct")]
    if marked_correct != [correct_letter]:
        mismatches.append((qid, correct_letter, marked_correct))

print(f"Checked {len(batch)} entries from {batch_file}")
print("missing ids (not in dump):", missing)
print("mismatches (id, expected_letter, marked_correct):", mismatches)
if not mismatches and not missing:
    print("ALL GOOD - 0 mismatches")
