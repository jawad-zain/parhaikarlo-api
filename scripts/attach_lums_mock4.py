"""One-off: create the LCAT Mock 4 MockTest row and attach its 120 questions.

Same pattern as scripts/attach_lums_mock3.py -- Mock 4 is a full-length mock,
so it belongs in quiz.MockTest, not content.PastPaper. Questions keep
past_paper=NULL and attach only through the MockTest M2M.

Matches by (question_text, option_a), like every other attach script, so it
works unchanged against a production DB whose PKs differ from local.

Idempotent: safe to re-run.
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

from content.models import Exam, Question  # noqa: E402
from quiz.models import MockTest  # noqa: E402

JSON_PATH = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_4.json"

# 7 sections at ~25 minutes each, per the source file's own header.
DURATION_MINUTES = 175


def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8-sig"))
    exam = Exam.objects.get(slug="lums")

    mt, created = MockTest.objects.get_or_create(
        exam=exam,
        name="LCAT Mock 4",
        kind="full",
        defaults={
            "duration_minutes": DURATION_MINUTES,
            "total_questions": len(data),
            "is_free": False,
            "is_active": True,
        },
    )
    print(f"MockTest: {'created' if created else 'already existed'} -- id={mt.id} name={mt.name!r}")

    found, missing = [], []
    for mcq in data:
        q = Question.objects.filter(
            subtopic__topic__subject__exam=exam,
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
        print("MISSING question_numbers:", missing)

    mt.questions.set(found)
    mt.total_questions = len(found)
    mt.duration_minutes = mt.duration_minutes or DURATION_MINUTES
    mt.save(update_fields=["total_questions", "duration_minutes"])
    print(
        f"MockTest {mt.id} ({mt.name}) now has {mt.questions.count()} questions, "
        f"total_questions={mt.total_questions}, duration={mt.duration_minutes} min, "
        f"is_free={mt.is_free}"
    )


if __name__ == "__main__":
    main()
