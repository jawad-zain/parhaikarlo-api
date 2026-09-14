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

IMPORTANT: groups are matched by (subject name, exact topic name), NOT by
numeric id. Topic ids are NOT consistent between local and production - a
first version of this script hardcoded local ids and, per a production
dry-run on 2026-09-15, those same ids point to entirely unrelated topics on
prod (e.g. local id=265 is Biology "Human Reproduction"; prod id=265 is a
Logical Reasoning topic "Letters and Symbol Series"). Matching by name is
safe regardless of what ids happen to be in a given environment.

Usage: python scripts/merge_biology_chemistry_duplicate_topics.py [--dry-run]
Idempotent: safe to re-run - once a group's duplicate names are gone, that
group is skipped (reported, not an error).
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()

from django.db import transaction

from content.models import Question, Subject, Topic

# (subject_name, canonical_topic_name, [duplicate_topic_names...])
GROUPS = [
    ("Biology", "Circulation", ["Human Physiology - Circulation", "Human Circulation"]),
    ("Biology", "Digestion", ["Human Physiology - Digestion", "Human Digestion"]),
    ("Biology", "Respiration", ["Human Physiology - Respiration", "Human Respiration"]),
    ("Biology", "Reproduction", ["Human Physiology - Reproduction", "Human Reproduction"]),
    ("Biology", "Human Physiology - Excretion", ["Human Excretion"]),  # no bare name exists
    ("Biology", "Cell Cycle & Division", ["Cell Cycle and Division", "Cell Division"]),
    ("Biology", "Cell Membrane & Transport", ["Cell Membrane and Transport"]),
    ("Biology", "Classification & Diversity", ["Classification and Diversity"]),
    ("Chemistry", "Thermochemistry", ["Thermochemistry and Energetics"]),
]


def get_topic_by_name(subject: Subject, name: str) -> Topic:
    """Exact, case-sensitive match on purpose - these names are known-exact
    from a live DB query, and a fuzzy match risks grabbing the wrong topic."""
    return Topic.objects.get(subject=subject, name=name)


def merge(dry_run: bool):
    for subject_name, canon_name, dup_names in GROUPS:
        subject = Subject.objects.get(name=subject_name)
        try:
            canon = get_topic_by_name(subject, canon_name)
        except Topic.DoesNotExist:
            print(f"SKIP group ({subject_name!r}/{canon_name!r}): canonical topic not found")
            continue

        print("=" * 70)
        print(f"CANONICAL: id={canon.id} {canon.name!r} (subject={subject_name})")

        canon_subs_by_name = {s.name.strip().lower(): s for s in canon.subtopics.all()}

        for dup_name in dup_names:
            try:
                dup = get_topic_by_name(subject, dup_name)
            except Topic.DoesNotExist:
                print(f"  SKIP dup {dup_name!r}: not found (already merged?)")
                continue

            # Sanity check: never merge a topic into itself.
            assert dup.id != canon.id, f"canonical and dup resolved to the same topic id {dup.id}"

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

            if dry_run:
                print(f"    (dry-run) would delete now-empty duplicate topic {dup.id}")
            else:
                remaining = dup.subtopics.count()
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
