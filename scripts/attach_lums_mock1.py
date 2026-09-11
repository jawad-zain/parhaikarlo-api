"""One-off: create the LCAT Mock 1 MockTest row and attach its 120 questions.

Why a quiz.MockTest and not a content.PastPaper: Mock 1 is a full-length mock,
so it belongs where the MDCAT mocks live (see scripts/attach_mockN.py). The
LUMS *sample* bank went to a PastPaper instead because it is LUMS' own
published sample paper, not a ParhaiKarlo-written mock.

Consequence worth knowing: mock questions keep past_paper=NULL and attach
only through the MockTest M2M. That means the stock
`manage.py load_explanations_by_content` command works for them directly --
it filters on past_paper__isnull=True, which is why the LUMS sample paper
needed the bespoke scripts/load_lums_sample_explanations.py and this bank
does not.

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

JSON_PATH = ROOT / "lums-content" / "parsed-mcqs" / "LUMS_MOCK_1.json"

# 7 sections at ~25 minutes each, per the source file's own header.
DURATION_MINUTES = 175


def main():
    data = json.loads(JSON_PATH.read_text(encoding="utf-8-sig"))
    exam = Exam.objects.get(slug="lums")

    mt, created = MockTest.objects.get_or_create(
        exam=exam,
        name="LCAT Mock 1",
        kind="full",
        defaults={
            "duration_minutes": DURATION_MINUTES,
            "total_questions": len(data),
            # Conservative default: not free. Flip with is_free=True if this
            # should be the free LUMS sample mock.
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
