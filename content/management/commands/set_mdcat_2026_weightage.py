"""Brings MDCAT Subject.weight_percent / question_count up to the 2026 pattern.

The seeded values were the 200-MCQ pattern used up to the 2024 paper
(Biology 68/34%, Chemistry 54/27%, Physics 54/27%, English 18/9%, Logical
Reasoning 6/3%). PMDC moved to a 180-MCQ paper with a different split, and
the 2025 paper in this database already follows it exactly — counted from
its own verified rows: Biology 81, Chemistry 45, Physics 36, English 9,
Logical Reasoning 9.

Those stale numbers were user-visible: /api/content/syllabus/ feeds the
frontend's /syllabus page and its Course JSON-LD, so the site was publishing
a weightage table that contradicted our own MDCAT 2026 syllabus post.

Idempotent — re-running writes the same values. Reports what changed.
"""

from django.core.management.base import BaseCommand

from content.models import Exam, Subject

# slug -> (question_count, weight_percent) for the MDCAT 2026 paper.
WEIGHTAGE = {
    'biology': (81, 45),
    'chemistry': (45, 25),
    'physics': (36, 20),
    'english': (9, 5),
    'logical-reasoning': (9, 5),
}


class Command(BaseCommand):
    help = 'Sets MDCAT subject weightage to the PMDC 2026 pattern (180 MCQs).'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true')

    def handle(self, *args, **options):
        dry = options['dry_run']
        try:
            exam = Exam.objects.get(slug='mdcat')
        except Exam.DoesNotExist:
            self.stderr.write(self.style.ERROR('No exam with slug "mdcat".'))
            return

        changed = 0
        for slug, (count, weight) in WEIGHTAGE.items():
            subject = Subject.objects.filter(exam=exam, slug=slug).first()
            if subject is None:
                self.stderr.write(self.style.WARNING(f'No subject "{slug}" under MDCAT - skipped.'))
                continue

            if subject.question_count == count and subject.weight_percent == weight:
                self.stdout.write(f'  {subject.name}: already {count} MCQs / {weight}%')
                continue

            self.stdout.write(
                f'  {subject.name}: {subject.question_count} MCQs / {subject.weight_percent}% '
                f'-> {count} MCQs / {weight}%'
            )
            if not dry:
                subject.question_count = count
                subject.weight_percent = weight
                subject.save(update_fields=['question_count', 'weight_percent'])
            changed += 1

        total = sum(c for c, _ in WEIGHTAGE.values())
        verb = 'Would update' if dry else 'Updated'
        self.stdout.write(self.style.SUCCESS(f'{verb} {changed} subject(s). Paper total: {total} MCQs.'))
