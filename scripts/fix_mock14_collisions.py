"""Fix the 9 (question_text, option_a) collisions found between mock 14
and mocks 1/2/4/7. For questions whose correct answer is NOT in slot A,
swap two non-correct option slots (content unchanged, breaks the dedupe
key, doesn't touch the correct letter). For questions whose correct
answer IS in slot A (ids 173, 169), swap A<->B (moves the correct letter
A->B) and compensate by swapping A<->B on two arbitrary non-colliding
B-correct questions elsewhere in the file (moving their correct letter
B->A), to keep the 45/45/45/45 balance intact.
"""
import ast
from pathlib import Path
from collections import Counter

SRC = Path(__file__).parent.parent / "mdcat-content" / "mdcat_mock_14.py"

src = SRC.read_text(encoding="utf-8")
tree = ast.parse(src)
ns = {}
exec(compile(tree, str(SRC), "exec"), ns)
questions = ns["QUESTIONS"]
qmap = {q["id"]: q for q in questions}

print("balance before:", dict(Counter(q["answer"] for q in questions)))

# Collision ids (mock14 side) and their non-correct-slot swap plan
SIMPLE_SWAP_IDS = {
    79: ("A", "D"),   # answer C, swap A/D
    134: ("A", "C"),  # answer B, swap A/C
    172: ("A", "B"),  # answer D, swap A/B
    175: ("A", "D"),  # answer C, swap A/D
    163: ("A", "B"),  # answer C, swap A/B
    164: ("A", "B"),  # answer D, swap A/B
    179: ("A", "B"),  # answer C, swap A/B
}

for qid, (x, y) in SIMPLE_SWAP_IDS.items():
    q = qmap[qid]
    assert q["answer"] not in (x, y), f"unsafe swap for {qid}"
    opts = q["options"]
    opts[x], opts[y] = opts[y], opts[x]

# A-correct collision ids: swap A<->B (answer becomes B)
A_CORRECT_IDS = [173, 169]
COLLIDING_IDS = set(SIMPLE_SWAP_IDS) | set(A_CORRECT_IDS)

for qid in A_CORRECT_IDS:
    q = qmap[qid]
    assert q["answer"] == "A"
    opts = q["options"]
    opts["A"], opts["B"] = opts["B"], opts["A"]
    q["answer"] = "B"

# Compensate: pick 2 arbitrary B-correct questions NOT in the colliding set,
# swap A<->B on them too (their correct letter moves B->A).
compensated = 0
for q in questions:
    if compensated >= len(A_CORRECT_IDS):
        break
    if q["id"] in COLLIDING_IDS:
        continue
    if q["answer"] == "B":
        opts = q["options"]
        opts["A"], opts["B"] = opts["B"], opts["A"]
        q["answer"] = "A"
        compensated += 1
        print(f"  compensated via id {q['id']}")

print("balance after:", dict(Counter(q["answer"] for q in questions)))
assert compensated == len(A_CORRECT_IDS)

# --- rewrite file ---
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
