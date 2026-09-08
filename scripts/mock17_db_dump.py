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

mt = MockTest.objects.get(name="MDCAT Mock 17")
qs = mt.questions.all().order_by("paper_order")
out = []
for q in qs:
    out.append({
        "id": q.id,
        "paper_order": q.paper_order,
        "subject": q.subtopic.topic.subject.name,
        "topic": q.subtopic.topic.name,
        "question_text": q.question_text,
        "options": {"a": q.option_a, "b": q.option_b, "c": q.option_c, "d": q.option_d},
        "correct_answer": q.correct_answer,
    })

out_path = ROOT / "scripts" / "mock17_db_dump.json"
out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"wrote {len(out)} rows to {out_path}")
