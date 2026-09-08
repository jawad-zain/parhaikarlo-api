import os
import sys
import hashlib
from pathlib import Path
from collections import Counter

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question
from quiz.models import MockTest

mt = MockTest.objects.get(name="MDCAT Mock 17")
qs = list(mt.questions.all())
print("total questions:", len(qs))
print("active:", sum(1 for q in qs if q.is_active), "verified:", sum(1 for q in qs if q.is_verified))

ids = sorted(q.id for q in qs)
print("id range:", ids[0], ids[-1], "contiguous:", ids == list(range(ids[0], ids[-1] + 1)))

orders = sorted(q.paper_order for q in qs)
print("paper_order clean 1-180 permutation:", orders == list(range(1, 181)))

print("answer balance:", dict(Counter(q.correct_answer for q in qs)))

# DB-wide (question_text, option_a) collision check
seen = {}
dupes = []
for q in Question.objects.all().only("id", "question_text", "option_a"):
    key = (q.question_text, q.option_a)
    if key in seen:
        dupes.append((seen[key], q.id))
    else:
        seen[key] = q.id
print("DB-wide dup (question_text, option_a) groups:", len(dupes))
mock17_ids = set(ids)
involving_17 = [d for d in dupes if d[0] in mock17_ids or d[1] in mock17_ids]
print("dup groups involving mock17:", involving_17)

# MockTest question-id overlap
all_mts = list(MockTest.objects.filter(kind="full"))
overlap_found = False
for i in range(len(all_mts)):
    for j in range(i + 1, len(all_mts)):
        a = set(all_mts[i].questions.values_list("id", flat=True))
        b = set(all_mts[j].questions.values_list("id", flat=True))
        inter = a & b
        if inter:
            overlap_found = True
            print(f"OVERLAP between {all_mts[i].name} and {all_mts[j].name}: {inter}")
print("total MockTests (kind=full):", len(all_mts), "overlap found:", overlap_found)

# image checks
imgs = [q for q in qs if q.is_visual_required]
print("is_visual_required count:", len(imgs))
for q in imgs:
    qi = q.images.first() if hasattr(q, "images") else None

from content.models import QuestionImage
all_qi = QuestionImage.objects.all()
hashes = {}
dup_hash = []
missing_file = []
for qi in all_qi:
    try:
        p = qi.image.path
        if not os.path.exists(p):
            missing_file.append(qi.id)
            continue
        h = hashlib.md5(Path(p).read_bytes()).hexdigest()
        if h in hashes:
            dup_hash.append((hashes[h], qi.id))
        else:
            hashes[h] = qi.id
    except Exception as e:
        missing_file.append((qi.id, str(e)))
print("total QuestionImage rows:", all_qi.count())
print("missing files:", missing_file)
print("duplicate hash groups:", dup_hash)

# explanation_options empty check for mock17
empty_opts = [q.id for q in qs if not q.explanation_options]
print("mock17 empty explanation_options:", len(empty_opts))
