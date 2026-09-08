"""One-off fix: importing mdcat_mock17.py's Q112 ("The functional group
-COOH characterizes which class of organic compounds?", option_a
"Alcohols") accidentally matched the dedupe key (past_paper=NULL,
question_text, option_a) against Question id=2816 -- one of the 200
OLD, soft-deactivated mock_1 questions (is_active=False) described in
[[mdcat-mock-tests]] memory as retaining real AttemptQuestion history.
import_mcqs.py's update path silently reactivated it (is_active=True)
and overwrote its option_b/c/d, correct_answer, difficulty, and
paper_order with mock17's Q112 content.

This reverts id=2816 back to its deactivated status (matching its 199
siblings in the same old id block, id range 2714-2913) and restores its
paper_order to fit the gap in that old sequence (between neighbours
102 and 104). The original option_b/c/d/correct_answer values for this
one row are not recoverable (no source JSON backup exists for the old,
pre-rewrite mock_1 200Q content), but is_active/is_verified/paper_order
are restored to be consistent with the rest of that dead block, taking
it back out of live circulation.
"""
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question

q = Question.objects.get(id=2816)
print("before:", q.is_active, q.is_verified, q.paper_order, q.correct_answer)
q.is_active = False
q.is_verified = True
q.paper_order = 103
q.save(update_fields=["is_active", "is_verified", "paper_order"])
q.refresh_from_db()
print("after:", q.is_active, q.is_verified, q.paper_order, q.correct_answer)
