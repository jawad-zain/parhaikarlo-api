"""Verify LCAT Mock 2 landed in the DB correctly. Read-only; safe to re-run.

Checks, against lums-content/raw-sources/lums_mock_02.py as the source of truth:
  1. all 120 questions exist, exactly once each
  2. every stored correct_answer matches the source key
  3. every stored option text matches the source, letter for letter
     (catches the option-swap/merge corruption class seen in MDCAT papers)
  4. every row is is_active and is_verified, so the quiz API can serve it
  5. all four explanation fields are populated
  6. each explanation's "Correct" label sits on the row's real correct_answer
  7. the MockTest row exists with all 120 attached and a sane duration
  8. answer-letter balance is even enough that guessing one letter does not pay
"""
import importlib.util
import os
import sys
from collections import Counter
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question  # noqa: E402
from quiz.models import MockTest  # noqa: E402

SRC = ROOT / "lums-content" / "raw-sources" / "lums_mock_02.py"
spec = importlib.util.spec_from_file_location("lums_mock_02_verify", SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
QUESTIONS = mod.QUESTIONS


def main():
    problems = []

    for sq in QUESTIONS:
        qs = Question.objects.filter(
            subtopic__topic__subject__exam__slug="lums",
            question_text=sq["question"],
            option_a=sq["options"]["A"],
        )
        n = qs.count()
        if n != 1:
            problems.append(f"Q{sq['id']}: found {n} DB rows, expected 1")
            continue
        q = qs.first()

        if (q.correct_answer or "").upper() != sq["answer"]:
            problems.append(
                f"Q{sq['id']} (db id={q.id}): correct_answer is "
                f"{q.correct_answer!r}, source key is {sq['answer']!r}"
            )
        for letter in "ABCD":
            stored = getattr(q, f"option_{letter.lower()}")
            if stored != sq["options"][letter]:
                problems.append(
                    f"Q{sq['id']} (db id={q.id}): option {letter} text differs from source"
                )
        if not q.is_active:
            problems.append(f"Q{sq['id']} (db id={q.id}): is_active is False")
        if not q.is_verified:
            problems.append(f"Q{sq['id']} (db id={q.id}): is_verified is False -- quiz API will hide it")

        for field in ("explanation_short", "explanation_long", "explanation_trick"):
            if not getattr(q, field):
                problems.append(f"Q{sq['id']} (db id={q.id}): {field} is empty")
        opts = q.explanation_options or {}
        if set(opts) != set("abcd"):
            problems.append(f"Q{sq['id']} (db id={q.id}): explanation_options keys are {sorted(opts)}")
        else:
            corr = [k for k, v in opts.items() if str(v).strip().lower().startswith("correct")]
            if len(corr) != 1:
                problems.append(
                    f"Q{sq['id']} (db id={q.id}): {len(corr)} options labelled Correct"
                )
            elif corr[0].lower() != (q.correct_answer or "").lower():
                problems.append(
                    f"Q{sq['id']} (db id={q.id}): explanation marks {corr[0].upper()} correct "
                    f"but correct_answer is {(q.correct_answer or '').upper()}"
                )

    mt = MockTest.objects.filter(exam__slug="lums", name="LCAT Mock 2").first()
    if not mt:
        problems.append("MockTest 'LCAT Mock 2' not found")
    else:
        attached = mt.questions.count()
        if attached != len(QUESTIONS):
            problems.append(f"MockTest has {attached} questions attached, expected {len(QUESTIONS)}")
        if mt.total_questions != len(QUESTIONS):
            problems.append(f"MockTest.total_questions is {mt.total_questions}, expected {len(QUESTIONS)}")
        if not mt.duration_minutes:
            problems.append("MockTest.duration_minutes is unset")
        if not mt.is_active:
            problems.append("MockTest.is_active is False")

    balance = Counter(sq["answer"] for sq in QUESTIONS)
    top = max(balance.values())
    if top > len(QUESTIONS) * 0.35:
        problems.append(
            f"answer-letter balance is skewed: {dict(sorted(balance.items()))} "
            f"-- guessing the commonest letter scores {top / len(QUESTIONS):.0%}"
        )

    print(f"source questions: {len(QUESTIONS)}")
    print(f"answer-letter balance: {dict(sorted(balance.items()))}")
    if mt:
        print(
            f"MockTest id={mt.id} {mt.name!r} kind={mt.kind} attached={mt.questions.count()} "
            f"duration={mt.duration_minutes} is_free={mt.is_free} is_active={mt.is_active}"
        )

    if problems:
        print(f"\nFAILED -- {len(problems)} problem(s):")
        for p in problems[:40]:
            print("  -", p)
        sys.exit(1)

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
