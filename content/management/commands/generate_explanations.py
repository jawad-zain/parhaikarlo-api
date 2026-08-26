import time

from django.core.management.base import BaseCommand, CommandError

from content.models import Question, PastPaper
from ai_tutor.services import generate_explanation


class Command(BaseCommand):
    help = "Generate + cache AI explanations (short/long/trick/options) for every active, verified question in a past paper's year."

    def add_arguments(self, parser):
        parser.add_argument("--year", type=int, required=True)
        parser.add_argument(
            "--overwrite",
            action="store_true",
            help="Regenerate even if an explanation is already cached.",
        )

    def handle(self, *args, **options):
        year = options["year"]
        overwrite = options["overwrite"]

        try:
            paper = PastPaper.objects.get(exam__slug="mdcat", year=year)
        except PastPaper.DoesNotExist:
            raise CommandError(f"No MDCAT past paper found for year {year}.")

        questions = Question.objects.filter(
            past_paper=paper,
            is_active=True,
            is_verified=True,
        ).order_by("id")

        if not overwrite:
            questions = questions.filter(explanation_options={})

        total = questions.count()
        self.stdout.write(f"Generating explanations for {total} questions in MDCAT {year}...")

        done = 0
        failed = 0

        for question in questions:
            try:
                generate_explanation(question)
                done += 1
            except Exception as e:
                failed += 1
                self.stderr.write(self.style.ERROR(f"Q{question.id} failed: {e}"))
            else:
                if done % 10 == 0:
                    self.stdout.write(f"  {done}/{total} done")

            time.sleep(0.3)  # stay well under Groq rate limits

        self.stdout.write(
            self.style.SUCCESS(f"Done. {done} generated, {failed} failed, out of {total}.")
        )
