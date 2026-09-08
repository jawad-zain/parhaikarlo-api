"""Fix the 9 cross-mock (question_text, option_a) collisions found by
check_mock18_collisions.py, by editing mdcat_mock_18.py in place.

For collisions where the correct answer is NOT in slot A: swap option_a
with a different non-correct slot (changes option_a's text, leaves the
correct answer's letter and content untouched).

For collisions where the correct answer IS in slot A (ids 61, 169): swap
A<->B on that question (moves its correct answer to B), and to preserve
the 45/45/45/45 balance, also swap A<->B on one arbitrary other
B-correct, non-colliding question (moves its correct answer back to A).
"""
import ast
from pathlib import Path
from collections import Counter

SRC = Path(__file__).parent.parent / "mdcat-content" / "mdcat_mock_18.py"

src = SRC.read_text(encoding="utf-8")
tree = ast.parse(src)
ns = {}
exec(compile(tree, str(SRC), "exec"), ns)
questions = ns["QUESTIONS"]
by_id = {q["id"]: q for q in questions}

before = Counter(q["answer"] for q in questions)
print("before:", dict(before))

# collisions: id -> current answer letter
collisions = {
    169: "A", 61: "A",
    75: "C", 164: "D", 56: "D", 163: "C", 179: "C", 110: "B", 167: "C",
}

collision_ids = set(collisions)

# 1) non-A-correct collisions: swap A with a non-correct slot
for qid, ans in collisions.items():
    if ans == "A":
        continue
    q = by_id[qid]
    opts = q["options"]
    other_slot = "B" if ans != "B" else "C"
    opts["A"], opts[other_slot] = opts[other_slot], opts["A"]
    # answer letter unchanged (its content/slot untouched)

# 2) A-correct collisions: swap A<->B (moves answer to B), then find an
# arbitrary non-colliding B-correct question and swap its A<->B (moves
# its answer back to A) to keep the balance even.
a_correct_collisions = [qid for qid, ans in collisions.items() if ans == "A"]
compensators = []
for qid in a_correct_collisions:
    q = by_id[qid]
    opts = q["options"]
    opts["A"], opts["B"] = opts["B"], opts["A"]
    q["answer"] = "B"

    # find a compensator: a question currently answer=='B', not itself a
    # collision id, not already used as a compensator
    for cand in questions:
        if cand["answer"] == "B" and cand["id"] not in collision_ids and cand["id"] not in compensators:
            copts = cand["options"]
            copts["A"], copts["B"] = copts["B"], copts["A"]
            cand["answer"] = "A"
            compensators.append(cand["id"])
            break
    else:
        raise RuntimeError("no compensator found")

print("compensator ids used:", compensators)

after = Counter(q["answer"] for q in questions)
print("after:", dict(after))
assert all(v == 45 for v in after.values()), after

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
