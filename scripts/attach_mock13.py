"""One-off: create MockTest 'MDCAT Mock 13' and attach the freshly-imported
MDCAT_MOCK_13.json questions to it.
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
from content.models import Question, Exam

data = json.loads((ROOT / "mdcat-content" / "parsed-mcqs" / "MDCAT_MOCK_13.json").read_text(encoding="utf-8"))

exam = Exam.objects.get(slug="mdcat")
mt, created = MockTest.objects.get_or_create(
    exam=exam,
    name="MDCAT Mock 13",
    kind="full",
    defaults={"duration_minutes": 180, "total_questions": 180, "is_free": True},
)
print(f"MockTest {'created' if created else 'reused'}: id={mt.id}")

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
