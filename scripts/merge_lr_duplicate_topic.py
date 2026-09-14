"""One-off: merge the duplicate MDCAT Logical Reasoning topic "Letter and
Symbol Series" (singular, a naming typo) into the canonical "Letters and
Symbol Series" (plural) topic, by reparenting its subtopics rather than
touching any Question rows. Idempotent — if the duplicate topic is already
gone (e.g. already run), it's a no-op.

Usage (from backend/, venv active):
    python scripts/merge_lr_duplicate_topic.py
"""
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.db import transaction  # noqa: E402
from content.models import Topic  # noqa: E402


def main():
    dup = Topic.objects.filter(
        subject__exam__name="MDCAT",
        subject__name="Logical Reasoning",
        name="Letter and Symbol Series",
    ).first()
    if not dup:
        print("Duplicate topic not found — already merged, nothing to do.")
        return

    target = Topic.objects.get(
        subject__exam__name="MDCAT",
        subject__name="Logical Reasoning",
        name="Letters and Symbol Series",
    )

    with transaction.atomic():
        for st in list(dup.subtopics.all()):
            print(f"Reparenting subtopic {st.id} {st.name!r} -> topic {target.name!r}")
            st.topic = target
            st.save()
        remaining = dup.subtopics.count()
        if remaining == 0:
            dup.delete()
            print("Deleted empty duplicate topic.")
        else:
            print(f"WARNING: {remaining} subtopics still under duplicate topic, not deleting.")


if __name__ == "__main__":
    main()
