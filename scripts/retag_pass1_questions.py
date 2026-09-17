"""Re-tag the two mis-tagged questions reactivated on 2026-09-17.

Both were inactive for years carrying a subtopic that has nothing to do
with what they ask, so reactivating them would have filed an alpha-glucose
structure under "Structure of DNA" and an op-amp circuit under
"Rectification".

Kept out of sync_mdcat_snapshot.py on purpose: that tool never touches
tags, and subtopic ids differ between databases, so the match is by name.

    py -3.14 scripts/retag_pass1_questions.py           # dry run
    py -3.14 scripts/retag_pass1_questions.py --apply

Idempotent, and it refuses to guess: a question or subtopic it cannot find
by name is reported and skipped rather than matched loosely.
"""
import os
import sys

import django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from content.models import Question, Subtopic  # noqa: E402

apply_changes = '--apply' in sys.argv

# (match on question_text prefix, subject name, topic name, subtopic name)
RETAGS = [
    ("Which one of the following is the formula structure of D (α) glucose?",
     "Biology", "Biological Molecules", "Carbohydrates"),
    ("An input voltage Vin of 0.50 V is applied to an op-amp",
     "Physics", "Electronics", "Operational Amplifiers (OP-AMP)"),
]

problems = 0
for text_prefix, subject, topic, subtopic_name in RETAGS:
    questions = list(Question.objects.filter(question_text__startswith=text_prefix))
    if len(questions) != 1:
        print(f"SKIP — {len(questions)} questions match {text_prefix[:50]!r}")
        problems += 1
        continue
    question = questions[0]

    subtopics = list(Subtopic.objects.filter(
        name=subtopic_name,
        topic__name=topic,
        topic__subject__name=subject,
    ))
    if len(subtopics) != 1:
        print(f"SKIP — {len(subtopics)} subtopics named "
              f"{subject}/{topic}/{subtopic_name}")
        problems += 1
        continue
    subtopic = subtopics[0]

    if question.subtopic_id == subtopic.id:
        print(f"ok — q{question.id} already tagged {subtopic}")
        continue

    print(f"q{question.id}: {question.subtopic} -> {subtopic}")
    if apply_changes:
        question.subtopic = subtopic
        question.save(update_fields=['subtopic'])

if not apply_changes:
    print("\nDry run — nothing written. Re-run with --apply.")
sys.exit(1 if problems else 0)
