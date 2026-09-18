"""Re-file the MDCAT mocks' coarse Chemistry buckets into the real syllabus units.

Pass 4 (merge_duplicate_topics.py) folded the duplicate topic names but had to
leave three buckets alone: "Organic Chemistry" (121 active questions),
"Inorganic Chemistry" (60) and "Physical Chemistry" (40). They came from the
mock importer, and the source files carry the same coarse label, so there
was no finer tagging to restore — each question had to be read and placed.

That reading is in chemistry_coarse_retag.json, one entry per question:
its text and option A (the same content key sync_mdcat_snapshot.py uses,
because ids differ between local and production) and the target topic and
subtopic. Every target is an existing Chemistry unit; three subtopics are
new because nothing specific enough existed: "Reactivity of Alkynes",
"Combustion of Hydrocarbons" (Chemistry of Hydrocarbons) and "Solubility
and Solubility Curves" (Liquids). Examples of the calls made: -COOH / -OH /
-NH2 "which class" questions -> Functional Groups; carbonyl position ->
Aldehydes and Ketones; oxidation-state changes -> Electrochemistry >
Oxidation and Reduction; M1V1 neutralisation sums -> Stoichiometry;
colligative properties -> Liquids.

Questions move; nothing about them is edited. Only questions still sitting
in one of the three buckets are touched. A bucket is deleted only once it
is empty and no attempt or topic note points at it, so a question the map
does not know about keeps its bucket alive and is reported instead.

Deleting the buckets removes /syllabus/chemistry/{organic,inorganic,
physical}-chemistry; the frontend's next.config.ts redirects all three.

Idempotent. Set DRY_RUN = True to see the plan without saving.

    python manage.py shell -c "exec(open('scripts/retag_chemistry_coarse_buckets.py', encoding='utf-8').read())"
"""

import json
from collections import Counter

from django.db import transaction
from django.utils.text import slugify

from content.models import Question, Subtopic, Topic
from quiz.models import Attempt

DRY_RUN = False
SUBJECT = "Chemistry"
BUCKETS = ["Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry"]
MAP_FILE = "scripts/chemistry_coarse_retag.json"


def _subtopic(topic, name, log):
    st = topic.subtopics.filter(name=name).first()
    if st:
        return st
    base = slugify(name) or "subtopic"
    slug, n = base, 2
    while topic.subtopics.filter(slug=slug).exists():
        slug, n = "%s-%d" % (base, n), n + 1
    order = (topic.subtopics.order_by("-order").values_list("order", flat=True).first() or 0) + 1
    log.append("  created subtopic %s > %s" % (topic.name, name))
    return Subtopic.objects.create(topic=topic, name=name, slug=slug, order=order)


def run():
    entries = json.load(open(MAP_FILE, encoding="utf-8"))
    buckets = list(Topic.objects.filter(subject__name=SUBJECT, name__in=BUCKETS))
    log, moved, per_topic, unmatched = [], 0, Counter(), 0

    for e in entries:
        qs = Question.objects.filter(
            subtopic__topic__in=buckets,
            question_text=e["question_text"],
            option_a=e["option_a"],
        )
        if not qs.exists():
            unmatched += 1  # already moved, or not on this database
            continue
        target = Topic.objects.filter(subject__name=SUBJECT, name=e["topic"]).first()
        if target is None:
            raise RuntimeError("missing target topic %r" % e["topic"])
        st = _subtopic(target, e["subtopic"], log)
        n = qs.update(subtopic=st)
        moved += n
        per_topic[e["topic"]] += n

    for t in buckets:
        left = Question.objects.filter(subtopic__topic=t).count()
        blocked = Attempt.objects.filter(topic=t).exists() or Attempt.objects.filter(subtopic__topic=t).exists()
        if left:
            log.append("  KEPT '%s': %d question(s) not in the map" % (t.name, left))
        elif blocked or hasattr(t, "concept_note"):
            log.append("  KEPT '%s': empty, but an attempt or note references it" % t.name)
        else:
            t.delete()
            log.append("  deleted empty topic '%s'" % t.name)

    print("%s%d question(s) moved, %d map entries not found in a bucket" % ("DRY RUN: " if DRY_RUN else "", moved, unmatched))
    for name, n in per_topic.most_common():
        print("    %3d -> %s" % (n, name))
    for line in log:
        print(line)
    if DRY_RUN:
        raise _DryRun()


class _DryRun(Exception):
    pass


before = Question.objects.filter(subtopic__topic__subject__name=SUBJECT).count()
try:
    with transaction.atomic():
        run()
        after = Question.objects.filter(subtopic__topic__subject__name=SUBJECT).count()
        if after != before:
            raise RuntimeError("Chemistry question count changed %d -> %d; rolled back" % (before, after))
except _DryRun:
    print("DRY RUN: rolled back, nothing saved")
else:
    remaining = Topic.objects.filter(subject__name=SUBJECT, name__in=BUCKETS).count()
    print("Chemistry: %d questions, %d topics, %d coarse bucket(s) left" % (
        before, Topic.objects.filter(subject__name=SUBJECT).count(), remaining))
