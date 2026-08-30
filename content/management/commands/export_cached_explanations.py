import json

from django.core.management.base import BaseCommand

from content.models import Question


class Command(BaseCommand):
    help = (
        "Export cached AI explanations (short/long/trick/options) from Question "
        "rows to a JSON file, in the exact format load_explanations expects: "
        "[{\"id\": 123, \"short\": \"...\", \"long\": \"...\", "
        "\"trick\": \"...\", \"options\": {\"a\":\"...\",\"b\":\"...\",\"c\":\"...\",\"d\":\"...\"}}]. "
        "Useful for syncing cached explanations generated on one DB (e.g. local "
        "dev) into another (e.g. prod) via `load_explanations`, which upserts by id."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            type=str,
            default="cached_explanations.json",
            help="Path to write the exported JSON file to (default: cached_explanations.json).",
        )
        parser.add_argument(
            "--filter-year",
            type=int,
            default=None,
            help="Only export questions belonging to a PastPaper with this year.",
        )
        parser.add_argument(
            "--filter-mocktest",
            type=str,
            default=None,
            help="Only export questions fixed into a MockTest whose name matches this (exact match).",
        )

    def handle(self, *args, **options):
        qs = Question.objects.exclude(explanation_short="").exclude(
            explanation_short__isnull=True
        )

        year = options["filter_year"]
        if year is not None:
            qs = qs.filter(past_paper__year=year)

        mocktest_name = options["filter_mocktest"]
        if mocktest_name is not None:
            qs = qs.filter(fixed_in_mock_tests__name=mocktest_name)

        qs = qs.distinct()

        items = [
            {
                "id": q.id,
                "short": q.explanation_short,
                "long": q.explanation_long,
                "trick": q.explanation_trick,
                "options": q.explanation_options,
            }
            for q in qs.iterator()
        ]

        output_path = options["output"]
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

        self.stdout.write(
            self.style.SUCCESS(
                f"Exported {len(items)} cached explanations to {output_path}"
            )
        )
