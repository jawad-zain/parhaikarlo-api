"""Move MDCAT Mock 16's atomic-structure question back to Chemistry.

Mock 16 was the one full MDCAT mock whose subject mix did not match PMDC's
2026 pattern (180 MCQs: Biology 81, Chemistry 45, Physics 36, English 9,
Logical Reasoning 9). It sat at Physics 37 / Chemistry 44 because "The
nucleus of an atom contains:" — authored as Chemistry / Atomic Structure in
mdcat-content/mdcat_mock_16.py and in MDCAT_MOCK_16.json, and sitting at the
head of that mock's chemistry block — was imported under Physics / Nuclear
Physics / Nucleus. The source files are right; only the DB row was wrong.

This matters beyond tidiness: the site claims MDCAT mocks are "weighted
exactly like the real exam", and that claim has to be true of every mock,
not nineteen of twenty.

Idempotent — safe to re-run. Match is by question text, not id, so it works
against local and production alike.

    python manage.py shell -c "exec(open('scripts/fix_mock16_subject_tag.py').read())"
"""

from content.models import Question, Subtopic

TEXT = "The nucleus of an atom contains:"
WRONG = ("Physics", "Nuclear Physics", "Nucleus")
RIGHT = ("Chemistry", "Atomic Structure")

target = Subtopic.objects.filter(
    topic__subject__name=RIGHT[0], topic__name=RIGHT[1], name=RIGHT[1]
).first()

if target is None:
    print(f"SKIP: no {RIGHT[0]} / {RIGHT[1]} subtopic on this database")
else:
    moved = 0
    for q in Question.objects.filter(
        question_text=TEXT,
        fixed_in_mock_tests__name__icontains="Mock 16",
        subtopic__topic__subject__name=WRONG[0],
    ).distinct():
        print(f"  id={q.id}: {q.subtopic.topic.subject.name} / {q.subtopic.name} -> {RIGHT[0]} / {target.name}")
        q.subtopic = target
        q.save(update_fields=["subtopic"])
        moved += 1
    print(f"retagged {moved} question(s)" if moved else "nothing to do (already Chemistry)")

from quiz.models import MockTest  # noqa: E402
import collections  # noqa: E402

m = MockTest.objects.filter(name__icontains="Mock 16", exam__name="MDCAT").first()
if m:
    mix = collections.Counter(
        m.questions.filter(is_active=True).values_list("subtopic__topic__subject__name", flat=True)
    )
    expected = {"Biology": 81, "Chemistry": 45, "Physics": 36, "English": 9, "Logical Reasoning": 9}
    print(f"{m.name} mix: {dict(mix)}")
    print("MATCHES PMDC 180-MCQ SPLIT" if dict(mix) == expected else "STILL OFF PATTERN")
