import json
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from content.models import Question


class Command(BaseCommand):
    help = (
        "Bulk-load hand-authored explanations from a JSON file into Question rows. "
        "JSON format: [{\"id\": 123, \"short\": \"...\", \"long\": \"...\", "
        "\"trick\": \"...\", \"options\": {\"a\":\"...\",\"b\":\"...\",\"c\":\"...\",\"d\":\"...\"}}]"
    )

    def add_arguments(self, parser):
        parser.add_argument("json_path", type=str)

    def handle(self, *args, **options):
        path = options["json_path"]

        try:
            with open(path, encoding="utf-8") as f:
                items = json.load(f)
        except FileNotFoundError:
            raise CommandError(f"File not found: {path}")

        updated = 0
        missing = 0

        for item in items:
            try:
                q = Question.objects.get(id=item["id"])
            except Question.DoesNotExist:
                self.stderr.write(self.style.ERROR(f"Question {item['id']} not found"))
                missing += 1
                continue

            q.explanation_short = item["short"]
            q.explanation_long = item["long"]
            q.explanation_trick = item["trick"]
            q.explanation_options = item["options"]
            q.explanation_generated_at = timezone.now()
            q.save(
                update_fields=[
                    "explanation_short",
                    "explanation_long",
                    "explanation_trick",
                    "explanation_options",
                    "explanation_generated_at",
                    "updated_at",
                ]
            )
            updated += 1

        self.stdout.write(
            self.style.SUCCESS(f"Updated {updated} questions. {missing} missing.")
        )
