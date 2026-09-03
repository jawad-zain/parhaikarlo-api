"""One-off: mdcat_mock_14.py's answer key was skewed toward 'B'
(96/180, ~53%) and away from 'D' (4/180) -- an exploitable guessing
pattern. Rebalance each question's option order (swap the correct
option into a target letter slot, round-robin A/B/C/D) so the
correct-answer distribution comes out 45/45/45/45, then rewrite the
file in the same dict-literal style. Has 5 image-based questions, so
the "image" key is preserved on rewrite.
"""
import ast
from pathlib import Path

SRC = Path(__file__).parent.parent / "mdcat-content" / "mdcat_mock_14.py"

src = SRC.read_text(encoding="utf-8")
tree = ast.parse(src)
ns = {}
exec(compile(tree, str(SRC), "exec"), ns)
questions = ns["QUESTIONS"]

from collections import Counter
print("original balance:", dict(Counter(q["answer"] for q in questions)))

LETTERS = ["A", "B", "C", "D"]
target_cycle = LETTERS * ((len(questions) // 4) + 1)

for i, q in enumerate(questions):
    target = target_cycle[i]
    cur_correct = q["answer"]
    if cur_correct == target:
        continue
    opts = q["options"]
    opts[cur_correct], opts[target] = opts[target], opts[cur_correct]
    q["answer"] = target

balance = Counter(q["answer"] for q in questions)
print("new balance:", dict(balance))

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
