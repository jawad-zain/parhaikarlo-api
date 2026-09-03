import json

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from content.models import Question


class Command(BaseCommand):
    help = (
        "Like load_explanations, but matches each entry by "
        "(question_text, option_a) instead of a numeric id — for loading "
        "explanations authored/exported on one DB (e.g. local dev) into "
        "another DB (e.g. production) where the same content exists under "
        "different auto-increment PKs, such as a freshly-imported mock test. "
        "JSON format: [{\"question_text\": \"...\", \"option_a\": \"...\", "
        "\"short\": \"...\", \"long\": \"...\", \"trick\": \"...\", "
        "\"options\": {\"a\":\"...\",\"b\":\"...\",\"c\":\"...\",\"d\":\"...\"}}]"
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
        ambiguous = 0

        for item in items:
            matches = Question.objects.filter(
                past_paper__isnull=True,
                question_text=item["question_text"],
                option_a=item["option_a"],
            )
            count = matches.count()
            if count == 0:
                self.stderr.write(self.style.ERROR(
                    f"No match for: {item['question_text'][:60]!r}"
                ))
                missing += 1
                continue
            if count > 1:
                self.stderr.write(self.style.WARNING(
                    f"{count} matches for: {item['question_text'][:60]!r} — updating all"
                ))
                ambiguous += 1

            for q in matches:
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

        self.stdout.write(self.style.SUCCESS(
            f"Updated {updated} questions. {missing} missing. {ambiguous} ambiguous (>1 match)."
        ))
