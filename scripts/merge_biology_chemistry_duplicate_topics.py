"""
Merge Biology + Chemistry fragmented-name duplicate Topics into one canonical
Topic per content area, by reparenting Subtopics (never touching Question rows
directly - Questions follow their Subtopic automatically).

Background: mdcat-practice-question-banks / practice-bank-gap-analysis memory
found these topic-name splits (e.g. "Circulation" / "Human Physiology -
Circulation" / "Human Circulation") hold genuinely distinct content (0-3
question overlap out of 8-89 per topic) - this is a pure taxonomy/naming
fix, not a content dedupe.

User decisions (2026-09-15):
- Canonical name = the bare/original topic name where one exists.
- For Excretion (no bare name exists), canonical = "Human Physiology - Excretion".
- For Chemistry Thermochemistry, canonical = the bare "Thermochemistry".

Usage: python scripts/merge_biology_chemistry_duplicate_topics.py [--dry-run]
Idempotent: safe to re-run - duplicate topics are gone after the first run,
so a second run finds nothing to do.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()

from django.db import transaction

from content.models import Question, Subtopic, Topic

# (canonical_topic_id, [duplicate_topic_ids...])
GROUPS = [
    (57, [206, 260]),   # Biology: Circulation
    (110, [205, 259]),  # Biology: Digestion
    (103, [207, 261]),  # Biology: Respiration
    (61, [210, 265]),   # Biology: Reproduction
    (208, [262]),       # Biology: Human Physiology - Excretion (canonical, no bare name exists)
    (200, [256, 141]),  # Biology: Cell Cycle & Division
    (199, [255]),       # Biology: Cell Membrane & Transport
    (203, [257]),       # Biology: Classification & Diversity
    (214, [70]),        # Chemistry: Thermochemistry
]


def merge(dry_run: bool):
    for canon_id, dup_ids in GROUPS:
        canon = Topic.objects.select_related("subject").get(id=canon_id)
        print("=" * 70)
        print(f"CANONICAL: id={canon.id} {canon.name!r} (subject={canon.subject.name})")

        canon_subs_by_name = {s.name.strip().lower(): s for s in canon.subtopics.all()}

        for dup_id in dup_ids:
            dup = Topic.objects.get(id=dup_id)
            print(f"  merging DUP id={dup.id} {dup.name!r} ->")

            for sub in list(dup.subtopics.all()):
                key = sub.name.strip().lower()
                existing = canon_subs_by_name.get(key)

                if existing is not None:
                    # Name collision: move this subtopic's questions onto the
                    # existing canonical subtopic, then delete the now-empty
                    # duplicate subtopic (can't reparent it as-is - would
                    # violate the (topic, name) unique constraint).
                    q_count = Question.objects.filter(subtopic=sub).count()
                    print(
                        f"    subtopic {sub.id} {sub.name!r} COLLIDES with "
                        f"canonical subtopic {existing.id} - moving {q_count} "
                        f"question(s) onto it, then deleting {sub.id}"
                    )
                    if not dry_run:
                        with transaction.atomic():
                            Question.objects.filter(subtopic=sub).update(subtopic=existing)
                            sub.delete()
                else:
                    q_count = Question.objects.filter(subtopic=sub).count()
                    print(
                        f"    subtopic {sub.id} {sub.name!r} -> reparenting "
                        f"to topic {canon.id} ({q_count} questions follow)"
                    )
                    if not dry_run:
                        sub.topic = canon
                        sub.save(update_fields=["topic"])
                    canon_subs_by_name[key] = sub  # avoid double-handling if a later dup repeats this name

            remaining = dup.subtopics.count() if dry_run else dup.subtopics.count()
            if dry_run:
                print(f"    (dry-run) would delete now-empty duplicate topic {dup.id}")
            else:
                if remaining == 0:
                    dup.delete()
                    print(f"    deleted now-empty duplicate topic {dup.id}")
                else:
                    print(
                        f"    WARNING: topic {dup.id} still has {remaining} "
                        f"subtopic(s) left, not deleting - investigate"
                    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    merge(dry_run=args.dry_run)
