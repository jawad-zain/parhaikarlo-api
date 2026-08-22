"""One-off: 4 questions in mdcat_mock_4.py coincidentally share
(question_text, option_a) with existing questions from mocks 1-3 -- the
exact key import_mcqs.py dedupes on for past_paper IS NULL rows. Left
as-is, importing mock_4 would silently overwrite the earlier mock's
Question row instead of creating a new one.

These are genuinely different MCQs (different distractor sets / answer
letters), not true duplicates -- so the fix is to swap two option slots
that do NOT include the correct answer, for just these 4 questions. This
changes what's in slot A (breaking the collision) without touching
content, meaning, or which answer is correct, and keeps the answer-letter
balance untouched since the correct slot never moves.
"""
import re
from pathlib import Path

SRC = Path(__file__).parent.parent / "mdcat-content" / "mdcat_mock_4.py"
src = SRC.read_text(encoding="utf-8")

# (question id, letters to swap) -- chosen so the correct-answer letter is
# never one of the two swapped.
SWAPS = {
    1: ("A", "B"),      # correct = C
    103: ("A", "B"),    # correct = D
    134: ("A", "C"),    # correct = B
    144: ("A", "C"),    # correct = B
}

import ast

tree = ast.parse(src)
ns = {}
exec(compile(tree, str(SRC), "exec"), ns)
questions = {q["id"]: q for q in ns["QUESTIONS"]}

for qid, (l1, l2) in SWAPS.items():
    q = questions[qid]
    assert q["answer"] not in (l1, l2), f"Q{qid}: correct answer {q['answer']} is one of the swap letters!"
    opts = q["options"]
    old1, old2 = opts[l1], opts[l2]
    # Build an exact find/replace on the source text for this one question's
    # options dict -- safer than regenerating the whole file's formatting.
    pattern = re.compile(
        r'(\{"id":' + str(qid) + r',.*?"options":\{)'
        r'"A":' + re.escape(repr(opts["A"])) + r', '
        r'"B":' + re.escape(repr(opts["B"])) + r', '
        r'"C":' + re.escape(repr(opts["C"])) + r', '
        r'"D":' + re.escape(repr(opts["D"])) + r'\}',
        re.DOTALL,
    )
    new_vals = dict(opts)
    new_vals[l1], new_vals[l2] = old2, old1
    replacement = (
        r'\1"A":' + repr(new_vals["A"]) + ', '
        '"B":' + repr(new_vals["B"]) + ', '
        '"C":' + repr(new_vals["C"]) + ', '
        '"D":' + repr(new_vals["D"]) + '}'
    )
    new_src, n = pattern.subn(replacement, src, count=1)
    assert n == 1, f"Q{qid}: pattern did not match exactly once (matched {n})"
    src = new_src
    print(f"Q{qid}: swapped {l1}<->{l2} (correct stays at {q['answer']})")

SRC.write_text(src, encoding="utf-8")
print(f"rewrote {SRC}")
