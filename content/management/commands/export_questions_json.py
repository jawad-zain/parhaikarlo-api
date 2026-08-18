"""
Django management command to export all active questions to a JSON file.

Place at: content/management/commands/export_questions_json.py

Usage:
    python manage.py export_questions_json
    python manage.py export_questions_json --output questions.json
    python manage.py export_questions_json --paper 2015
    python manage.py export_questions_json --only-unverified
"""

import json
from pathlib import Path
from django.core.management.base import BaseCommand
from content.models import Question


class Command(BaseCommand):
    help = "Export active questions to JSON for offline verification"

    def add_arguments(self, parser):
        parser.add_argument("--output", default="questions.json")
        parser.add_argument("--paper", type=int, default=None)
        parser.add_argument("--only-unverified", action="store_true")
        parser.add_argument("--include-inactive", action="store_true")

    def handle(self, *args, **opts):
        qs = Question.objects.select_related(
            "past_paper", "subtopic__topic__subject"
        )
        if not opts["include_inactive"]:
            qs = qs.filter(is_active=True)
        if opts["only_unverified"]:
            qs = qs.filter(is_verified=False)
        if opts["paper"]:
            qs = qs.filter(past_paper__year=opts["paper"])

        qs = qs.order_by("past_paper__year", "id")
        total = qs.count()
        self.stdout.write(f"Exporting {total} questions...")

        rows = []
        for q in qs:
            st = q.subtopic
            tp = st.topic if st else None
            sj = tp.subject if tp else None
            rows.append({
                "id": q.id,
                "year": q.past_paper.year if q.past_paper else None,
                "subject": sj.name if sj else "",
                "topic": tp.name if tp else "",
                "subtopic": st.name if st else "",
                "question": q.question_text or "",
                "options": {
                    "A": q.option_a or "",
                    "B": q.option_b or "",
                    "C": q.option_c or "",
                    "D": q.option_d or "",
                },
                "stored_answer": (q.correct_answer or "").upper(),
                "verified_answer": None,  # <-- friends fill this in: "A" / "B" / "C" / "D"
                "is_verified": bool(q.is_verified),
            })

        out_path = Path(opts["output"])
        out_path.write_text(
            json.dumps(rows, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        self.stdout.write(self.style.SUCCESS(
            f"Wrote {total} Qs -> {out_path.resolve()}"
        ))