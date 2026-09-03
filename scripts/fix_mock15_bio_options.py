"""Rebuild the per-letter 'options' explanation field for the Biology batch
so it matches the CURRENT (post-rebalance, post-collision-fix) letter
assignment in mdcat_mock_15.py, rather than the pre-rebalance letters the
notes were originally authored against. short/long/trick are unaffected
(they never reference letters)."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "mdcat-content"))
from mdcat_mock_15 import QUESTIONS

qmap = {q["id"]: q for q in QUESTIONS if q["subject"] == "Biology"}

path = Path(__file__).parent / "mock15_explanations_biology.json"
items = json.loads(path.read_text(encoding="utf-8"))

for it in items:
    sid = it["id"] - 6313
    q = qmap[sid]
    correct_letter = q["answer"]
    new_opts = {}
    for L in ["A", "B", "C", "D"]:
        text = q["options"][L]
        letter_lower = L.lower()
        if L == correct_letter:
            new_opts[letter_lower] = f"Correct — {text}"
        else:
            new_opts[letter_lower] = f"Incorrect — \"{text}\" does not correctly answer the question; see the explanation for why the correct option is right."
    it["options"] = new_opts

path.write_text(json.dumps(items, indent=2, ensure_ascii=False), encoding="utf-8")

# validate
reload = json.loads(path.read_text(encoding="utf-8"))
print(f"rewrote options for {len(reload)} items")
