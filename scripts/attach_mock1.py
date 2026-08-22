"""One-off: attach the freshly-imported MDCAT_MOCK_1.json questions to
MockTest id=1, and update total_questions to match. Old (pre-rewrite)
mock_1 questions were already detached + deactivated separately.
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

from quiz.models import MockTest
from content.models import Question

data = json.loads((ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_MOCK_1.json").read_text(encoding="utf-8"))

mt = MockTest.objects.get(id=1)
found, missing = [], []
for mcq in data:
    q = Question.objects.filter(
        past_paper__isnull=True,
        question_text=mcq["question_text"],
        option_a=mcq["options"]["a"],
    ).first()
    if q:
        found.append(q)
    else:
        missing.append(mcq["question_number"])

print(f"matched {len(found)}/{len(data)} questions")
if missing:
    print("missing question_numbers:", missing)

mt.questions.set(found)
mt.total_questions = len(found)
mt.save(update_fields=["total_questions"])
print(f"MockTest {mt.id} ({mt.name}) now has {mt.questions.count()} questions attached, total_questions={mt.total_questions}")
