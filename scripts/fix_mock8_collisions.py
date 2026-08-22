"""One-off: 5 questions in mdcat_mock_8.py (post-rebalance) coincidentally
share (question_text, option_a) with existing questions from mocks 1-7 --
the DB dedupe key for past_paper IS NULL rows.

For the 3 collisions where the correct answer is NOT in slot A (80, 158, 164),
swap two non-correct option slots so option_a changes without touching the
correct answer's letter or content.

For the 2 collisions where the correct answer IS in slot A (129, 169), the
content itself must move out of slot A, so swap A<->B on those (correct
letter moves from A to B). To keep the answer-letter distribution at
45/45/45/45, two arbitrary non-colliding B-correct questions (2, 6) are
also swapped A<->B, moving their correct letter from B to A.
"""
import ast
from pathlib import Path

SRC = Path(__file__).parent.parent / "mdcat-content" / "mdcat_mock_8.py"

src = SRC.read_text(encoding="utf-8")
tree = ast.parse(src)
ns = {}
exec(compile(tree, str(SRC), "exec"), ns)
questions = ns["QUESTIONS"]
by_id = {q["id"]: q for q in questions}

NON_CORRECT_SWAPS = {
    80: ("A", "B"),   # correct = D
    158: ("A", "C"),  # correct = B
    164: ("A", "B"),  # correct = D
}
for qid, (l1, l2) in NON_CORRECT_SWAPS.items():
    q = by_id[qid]
    assert q["answer"] not in (l1, l2), f"Q{qid}: correct answer {q['answer']} is one of the swap letters!"
    opts = q["options"]
    opts[l1], opts[l2] = opts[l2], opts[l1]
    print(f"Q{qid}: swapped {l1}<->{l2} (correct stays at {q['answer']})")

CORRECT_MOVES_A_TO_B = [129, 169]
for qid in CORRECT_MOVES_A_TO_B:
    q = by_id[qid]
    assert q["answer"] == "A"
    opts = q["options"]
    opts["A"], opts["B"] = opts["B"], opts["A"]
    q["answer"] = "B"
    print(f"Q{qid}: swapped A<->B, correct moved A->B")

COMPENSATE_B_TO_A = [2, 6]
for qid in COMPENSATE_B_TO_A:
    q = by_id[qid]
    assert q["answer"] == "B"
    opts = q["options"]
    opts["A"], opts["B"] = opts["B"], opts["A"]
    q["answer"] = "A"
    print(f"Q{qid}: swapped A<->B, correct moved B->A (balance compensation)")

from collections import Counter
balance = Counter(q["answer"] for q in questions)
print("new balance:", dict(balance))

SUBJECT_BLOCKS = [
    ("BIOLOGY", 81),
    ("CHEMISTRY", 45),
    ("PHYSICS", 36),
    ("ENGLISH", 9),
    ("LOGICAL REASONING", 9),
]

LETTERS = ["A", "B", "C", "D"]


def fmt_options(opts):
    parts = ", ".join(f'"{L}":{opts[L]!r}' for L in LETTERS)
    return "{" + parts + "}"


lines = ["QUESTIONS = [", ""]
idx = 0
for name, count in SUBJECT_BLOCKS:
    lines.append("# " + "=" * 60)
    lines.append(f"# {name} ({count}) - id {questions[idx]['id']}-{questions[idx + count - 1]['id']}")
    lines.append("# " + "=" * 60)
    lines.append("")
    for q in questions[idx: idx + count]:
        lines.append(
            f'{{"id":{q["id"]},"subject":{q["subject"]!r},"topic":{q["topic"]!r},"difficulty":{q["difficulty"]!r},'
        )
        lines.append(f' "question":{q["question"]!r},')
        if "image" in q:
            lines.append(f' "image":{q["image"]!r},')
        lines.append(f' "options":{fmt_options(q["options"])},"answer":{q["answer"]!r}}},')
        lines.append("")
    idx += count

lines.append("]")
new_block = "\n".join(lines)

start = src.index("QUESTIONS = [")
end = src.index("\n]\n", start) + len("\n]\n")
new_src = src[:start] + new_block + "\n" + src[end:]

SRC.write_text(new_src, encoding="utf-8", newline="\n")
print(f"rewrote {SRC}")
