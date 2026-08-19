"""
Second pass for MDCAT 2012: clean option text for the 4 "strong"-marker questions
that got real images imported (2525, 2534, 2538, 2542), then reactivate + verify
them. correct_answer letters already match the official UHS 2012 key -- unchanged.

Run: python manage.py shell -c "exec(open('scripts/fix_2012_text2.py', encoding='utf-8').read())"
"""
from content.models import Question

FIXES = {
    # Q31 - displacement-time graph, "PR" segment (correct: B, matches key)
    2525: dict(
        option_a="Twice the frequency",
        option_b="Half the period",
        option_c="Half the frequency",
        option_d="Twice the period",
    ),
    # Q40 - logic symbol for a NOT Gate (correct: A, matches key)
    2534: dict(
        option_a="NOT gate symbol (triangle with a bubble at the output)",
        option_b="AND gate symbol",
        option_c="OR gate symbol",
        option_d="Diode symbol (not a logic gate)",
    ),
    # Q44 - I-V curve of a junction diode (correct: B, matches key)
    2538: dict(
        option_a="Steep S-shaped curve: near-zero current for negative V, rising sharply for positive V",
        option_b="Continuous curve through the origin, roughly linear with a slight bend at the origin",
        option_c="Straight line through the origin (perfectly linear/ohmic)",
        option_d="Two disconnected line segments, one in the third quadrant and one in the fourth quadrant",
    ),
    # Q48 - formula of alanine (correct: A, matches key)
    2542: dict(
        option_a="H2N-CH(CH3)-COOH",
        option_b="H2N-CH2-CH(NH2)-COOH",
        option_c="HOOC-CH2-CH(NH2)-COOH",
        option_d="H2N-CH2-(CH2)3-CH(NH2)-COOH",
    ),
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
