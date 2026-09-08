"""Seed the LUMS Exam + Subject rows.

LUMS has no committed seed for MDCAT to mirror (its Exam/Subject rows predate
this repo's migration history and were never captured in a script) — this
command is the equivalent for LUMS, written as get_or_create so it's safe to
re-run.

Subject scope as of 2026-09-08: Verbal + Math only. That's everything the one
piece of source material we have (LUMS' own "Sample Questions for Verbal &
Math Sections" guide, 24 Qs total) actually evidences for the LUMS Common
Admission Test (LCAT). Do NOT add Analytical Reasoning / Physics / Chemistry
here until a real LCAT source document shows those sections — see
lums-content/README.md.

weight_percent and question_count are left at 0 (unknown) rather than
extrapolated from a 24-question sample bank pretending to be a full paper —
a wrong number here "locks in bad dashboards for months" (see the MDCAT
lesson this mirrors). Fill these in once a real, full-length, dated LCAT past
paper has been reviewed.
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from content.models import Exam, Subject


SUBJECTS = [
    # name, order
    ("Verbal", 1),
    ("Math", 2),
]


class Command(BaseCommand):
    help = "Seed the LUMS Exam row and its Subjects (Verbal, Math). Idempotent."

    def add_arguments(self, parser):
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Print what would be created/updated without writing to the DB.",
        )

    def handle(self, *args, **opts):
        dry_run = opts["dry_run"]

        self.stdout.write("Exam:")
        self.stdout.write("  name=LUMS slug=lums board=University level=entry-test is_active=True")
        if dry_run:
            exam = Exam(name="LUMS", slug="lums", board="University", level="entry-test", is_active=True)
        else:
            exam, created = Exam.objects.get_or_create(
                slug="lums",
                defaults={
                    "name": "LUMS",
                    "board": "University",
                    "level": "entry-test",
                    "is_active": True,
                },
            )
            self.stdout.write(self.style.SUCCESS(f"  {'created' if created else 'already existed'}"))

        self.stdout.write("\nSubjects:")
        for name, order in SUBJECTS:
            slug = slugify(name)
            self.stdout.write(f"  name={name} slug={slug} order={order} weight_percent=0 question_count=0")
            if dry_run:
                continue
            subject, created = Subject.objects.get_or_create(
                exam=exam,
                name=name,
                defaults={
                    "slug": slug,
                    "order": order,
                    "weight_percent": 0,
                    "question_count": 0,
                    "is_active": True,
                },
            )
            self.stdout.write(self.style.SUCCESS(f"    {'created' if created else 'already existed'}"))

        if dry_run:
            self.stdout.write(self.style.WARNING("\nDRY RUN — nothing written."))
