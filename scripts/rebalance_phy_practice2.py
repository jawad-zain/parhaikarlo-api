"""
Surgical in-place rebalance of mdcat_phy_practice2.py's answer-letter
distribution to an exact 50/50/50/50 A/B/C/D split, WITHOUT touching any
other text in the file (question text, topic/difficulty, "image" keys,
comments, formatting) -- same pattern used for english_practice.py.

Only the "options":{...},"answer":"X" substring of each of the 200
question entries is rewritten, in file order, using a regex over the
simple `"options":{"A":"...","B":"...","C":"...","D":"..."},"answer":"X"`
pattern (verified beforehand: no embedded literal quotes in any option
text, so this simple non-greedy regex is safe).
"""
import re
import random
from pathlib import Path

FILE = Path(__file__).parent.parent / "mdcat-content" / "mdcat_phy_practice2.py"

PATTERN = re.compile(
    r'"options":\{"A":"([^"]*)","B":"([^"]*)","C":"([^"]*)","D":"([^"]*)"\},"answer":"([ABCD])"'
)


def main():
    text = FILE.read_text(encoding="utf-8")
    matches = list(PATTERN.finditer(text))
    n = len(matches)
    assert n == 200, f"expected 200 matches, got {n}"

    # Build an exact 50/50/50/50 target-letter list and shuffle it (seed 42,
    # matching the convention used for the other rebalanced practice banks).
    target_letters = ["A"] * 50 + ["B"] * 50 + ["C"] * 50 + ["D"] * 50
    random.seed(42)
    random.shuffle(target_letters)

    pieces = []
    last_end = 0
    for i, m in enumerate(matches):
        a, b, c, d, orig_letter = m.groups()
        opts = {"A": a, "B": b, "C": c, "D": d}
        correct_text = opts[orig_letter]
        distractors = [opts[L] for L in "ABCD" if L != orig_letter]

        target = target_letters[i]
        # Assign correct_text to `target`, and the 3 distractors to the
        # remaining letters in a fixed order (A,B,C,D minus target).
        remaining_letters = [L for L in "ABCD" if L != target]
        new_opts = {target: correct_text}
        for L, txt in zip(remaining_letters, distractors):
            new_opts[L] = txt

        new_block = (
            '"options":{'
            f'"A":"{new_opts["A"]}","B":"{new_opts["B"]}",'
            f'"C":"{new_opts["C"]}","D":"{new_opts["D"]}"'
            '},"answer":"' + target + '"'
        )

        pieces.append(text[last_end:m.start()])
        pieces.append(new_block)
        last_end = m.end()
    pieces.append(text[last_end:])

    new_text = "".join(pieces)
    FILE.write_text(new_text, encoding="utf-8")
    print(f"Rewrote {n} question entries in {FILE}")
    from collections import Counter
    print("New target-letter balance:", Counter(target_letters))


if __name__ == "__main__":
    main()
