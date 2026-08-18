import re
from pathlib import Path
from django.core.management.base import BaseCommand
from django.db import transaction
from content.models import Question

LINE_RE = re.compile(r'^\s*ID\s+(\d+)\s*:\s*([A-Da-d])\b')

class Command(BaseCommand):
    help = "Apply verified answer keys from keys.txt (format: 'ID <pk>: <letter> (...)')"

    def add_arguments(self, parser):
        parser.add_argument('keys_file', type=str, help='Path to keys.txt')
        parser.add_argument('--apply', action='store_true',
                            help='Actually write changes. Omit for dry-run.')

    def handle(self, *args, **opts):
        path = Path(opts['keys_file'])
        apply = opts['apply']

        updated, unchanged, missing, bad = 0, 0, 0, []

        with path.open(encoding='utf-8') as f:
            lines = f.readlines()

        with transaction.atomic():
            for lineno, raw in enumerate(lines, 1):
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                m = LINE_RE.match(line)
                if not m:
                    # skip section headers / comments silently
                    continue
                qid = int(m.group(1))
                letter = m.group(2).upper()

                try:
                    q = Question.objects.get(pk=qid)
                except Question.DoesNotExist:
                    missing += 1
                    self.stdout.write(self.style.WARNING(f"line {lineno}: ID {qid} not in DB"))
                    continue

                if q.correct_answer == letter:
                    unchanged += 1
                    continue

                self.stdout.write(f"ID {qid}: {q.correct_answer} -> {letter}")
                if apply:
                    q.correct_answer = letter
                    q.is_verified = True
                    q.save(update_fields=['correct_answer', 'is_verified'])
                updated += 1

            if not apply:
                transaction.set_rollback(True)

        mode = "APPLIED" if apply else "DRY-RUN (nothing saved)"
        self.stdout.write(self.style.SUCCESS(
            f"\n[{mode}] flipped={updated} unchanged={unchanged} missing={missing}"
        ))
        if not apply:
            self.stdout.write("Re-run with --apply to persist.")
            