"""Fix the 3 (question_text, option_a) collisions found between mock 15
and mocks 2/4/7 (ids 130, 22, 82 -- all correct answer B). Swap two
non-correct option slots (content unchanged, breaks the dedupe key on
option_a, doesn't touch the correct letter or balance).
"""
import ast
from pathlib import Path
from collections import Counter

SRC = Path(__file__).parent.parent / "mdcat-content" / "mdcat_mock_15.py"

src = SRC.read_text(encoding="utf-8")
tree = ast.parse(src)
ns = {}
exec(compile(tree, str(SRC), "exec"), ns)
questions = ns["QUESTIONS"]
qmap = {q["id"]: q for q in questions}

print("balance before:", dict(Counter(q["answer"] for q in questions)))

SIMPLE_SWAP_IDS = {
    130: ("A", "C"),  # answer B, swap A/C
    22: ("A", "D"),   # answer B, swap A/D
    82: ("A", "C"),   # answer B, swap A/C (matches CD swap avoidance)
}

for qid, (x, y) in SIMPLE_SWAP_IDS.items():
    q = qmap[qid]
    assert q["answer"] not in (x, y), f"unsafe swap for {qid}"
    opts = q["options"]
    opts[x], opts[y] = opts[y], opts[x]

print("balance after:", dict(Counter(q["answer"] for q in questions)))

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
