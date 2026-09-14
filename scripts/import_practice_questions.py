"""Generic import for a practice-question export produced by
export_mdcat_practice.py (or export_lums_practice.py) — content-matched on
(question_text, option_a) so it's safe to re-run without creating
duplicates. Creates any missing Subject/Topic/Subtopic rows it needs.

Usage (from backend/, venv active):
    python scripts/import_practice_questions.py mdcat_practice_export.json --dry-run
    python scripts/import_practice_questions.py mdcat_practice_export.json
"""
import argparse
import json
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.utils.text import slugify  # noqa: E402
from content.models import Exam, Subject, Topic, Subtopic, Question  # noqa: E402


def get_or_create_subtopic(exam_name, subject_name, topic_name, subtopic_name):
    exam = Exam.objects.get(name=exam_name)
    subject, _ = Subject.objects.get_or_create(
        exam=exam, name=subject_name,
        defaults={"slug": slugify(subject_name)},
    )
    topic, _ = Topic.objects.get_or_create(
        subject=subject, name=topic_name,
        defaults={"slug": slugify(topic_name)},
    )
    subtopic, _ = Subtopic.objects.get_or_create(
        topic=topic, name=subtopic_name,
        defaults={"slug": slugify(subtopic_name)},
    )
    return subtopic


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--dry-run", action="store_true")
    opts = ap.parse_args()

    rows = json.loads(Path(opts.input).read_text(encoding="utf-8"))
    print(f"Loaded {len(rows)} questions from {opts.input}")

    created, skipped = 0, 0
    for r in rows:
        exists = Question.objects.filter(
            question_text=r["question_text"],
            option_a=r["option_a"],
        ).exists()
        if exists:
            skipped += 1
            continue

        created += 1
        if opts.dry_run:
            continue

        subtopic = get_or_create_subtopic(
            r["exam"], r["subject"], r["topic"], r["subtopic"]
        )
        Question.objects.create(
            subtopic=subtopic,
            question_text=r["question_text"],
            option_a=r["option_a"],
            option_b=r["option_b"],
            option_c=r["option_c"],
            option_d=r["option_d"],
            correct_answer=r["correct_answer"],
            difficulty=r.get("difficulty", "medium"),
            is_verified=r.get("is_verified", False),
            is_active=r.get("is_active", True),
            explanation_short=r.get("explanation_short", ""),
            explanation_long=r.get("explanation_long", ""),
            explanation_trick=r.get("explanation_trick", ""),
            explanation_options=r.get("explanation_options", {}),
        )

    verb = "would create" if opts.dry_run else "created"
    print(f"{verb}: {created}  skipped (already present, content-matched): {skipped}")


if __name__ == "__main__":
    main()
