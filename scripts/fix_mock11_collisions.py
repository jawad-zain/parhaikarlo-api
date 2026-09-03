"""One-off: 2 questions in mdcat_mock11.py coincidentally share
(question_text, option_a) with existing questions from Mock 9 -- the DB
dedupe key for past_paper IS NULL rows.

Q96 (correct=D): option_a is a distractor, so swap A<->B (correct answer
stays untouched in D).

Q177 (correct=A): the correct answer's own content sits in slot A, so it
must move out of A -- swap A<->B (correct moves A->B). To keep the
answer-letter distribution at 45/45/45/45, a non-colliding B-correct
question (Q2) is also swapped A<->B (correct moves B->A) to compensate.
"""
import ast
from pathlib import Path

SRC = Path(__file__).parent.parent / "mdcat-content" / "mdcat_mock11.py"

src = SRC.read_text(encoding="utf-8")
tree = ast.parse(src)
ns = {}
exec(compile(tree, str(SRC), "exec"), ns)
questions = ns["QUESTIONS"]
by_id = {q["id"]: q for q in questions}

q = by_id[96]
assert q["answer"] == "D"
opts = q["options"]
opts["A"], opts["B"] = opts["B"], opts["A"]
print(f"Q96: swapped A<->B (correct stays at {q['answer']})")

q = by_id[177]
assert q["answer"] == "A"
opts = q["options"]
opts["A"], opts["B"] = opts["B"], opts["A"]
q["answer"] = "B"
print("Q177: swapped A<->B, correct moved A->B")

q = by_id[2]
assert q["answer"] == "B"
opts = q["options"]
opts["A"], opts["B"] = opts["B"], opts["A"]
q["answer"] = "A"
print("Q2: swapped A<->B, correct moved B->A (balance compensation)")

from collections import Counter
balance = Counter(q["answer"] for q in questions)
print("new balance:", dict(balance))

LETTERS = ["A", "B", "C", "D"]

SUBJECT_BLOCKS = [
    ("BIOLOGY", 81),
    ("CHEMISTRY", 45),
    ("PHYSICS", 36),
    ("ENGLISH", 9),
    ("LOGICAL REASONING", 9),
]


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
