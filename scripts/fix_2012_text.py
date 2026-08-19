"""
One-off fix for MDCAT 2012: rewrite OCR-garbled option text for questions whose
answer letter already matches the official UHS 2012 answer key (verified against
the authentic mdcatguide.com scan), so no correct_answer changes are needed here
-- just clean, accurate option text. Also reactivates + verifies these rows since
they were previously deactivated by the importer due to leftover OCR placeholder
markers.

Run: python manage.py shell < scripts/fix_2012_text.py   (from backend/)
"""
from content.models import Question

FIXES = {
    # Q19 - dimensions of x = mc^2 (correct: B, matches key)
    2513: dict(
        option_a="[LT⁻¹]",
        option_b="[ML²T⁻²]",
        option_c="[MLT⁻¹]",
        option_d="[MLT⁻²]",
    ),
    # Q29 - SHM acceleration equation, T = 10s (correct: C, matches key)
    2523: dict(
        option_a="a = -2x",
        option_b="a = -(20π)x",
        option_c="a = -(2π/10)²x",
        option_d="a = -(20π)²x",
    ),
    # Q32 - Doppler apparent frequency, source moving towards observer (correct: B, matches key)
    2526: dict(
        option_a="fo = ((v+ui)/v) f",
        option_b="fo = (v/(v-ui)) f",
        option_c="fo = (v/(v+ui)) f",
        option_d="fo = ((v-ui)/v) f",
    ),
    # Q36 - mean square speed of N gas molecules (correct: A, matches key)
    2530: dict(
        option_a="(v1 + v2 + ... + vx) / N",
        option_b="(v1² + v2² + ... + vx²) / N",
        option_c="√[(v1 + v2 + ... + vx) / N]",
        option_d="√[(v1² + v2² + ... + vx²) / N]",
    ),
    # Q107 SPOT THE ERROR (correct: D, matches key)
    2601: dict(option_a="discarded", option_b="as", option_c="there", option_d="for"),
    # Q108 SPOT THE ERROR (correct: D, matches key)
    2602: dict(option_a="raising", option_b="much", option_c="demands", option_d="away"),
    # Q109 SPOT THE ERROR (correct: A, matches key)
    2603: dict(option_a="from", option_b="bruises", option_c="Thank", option_d="was"),
    # Q110 SPOT THE ERROR (correct: A, matches key)
    2604: dict(option_a="for", option_b="to", option_c="grown", option_d="over"),
    # Q111 SPOT THE ERROR (correct: A, matches key)
    2605: dict(option_a="me", option_b="greeted", option_c="a", option_d="of"),
    # Q112 SPOT THE ERROR (correct: D, matches key)
    2606: dict(option_a="destroys", option_b="in", option_c="the", option_d="cause"),
}

updated = 0
for qid, opts in FIXES.items():
    q = Question.objects.get(id=qid)
    for field, val in opts.items():
        setattr(q, field, val)
    q.is_active = True
    q.is_verified = True
    q.save()
    updated += 1

print(f"updated {updated} questions")
