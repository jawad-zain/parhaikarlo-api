"""Audit every MDCAT past paper for questions that need a diagram/image
but do not have one verified in the DB yet.

Two signals are used:
  - STRONG: question_text still carries the parser's
    "[Diagram/graph/structure required ...]" marker, meaning OCR
    could not transcribe a figure that the question depends on.
  - WEAK: question_text matches one of the candidate keywords used by
    review_visual_questions.py (figure, graph, "shown below", etc.)
    without necessarily being un-transcribable.

For every candidate, checks whether a QuestionImage row exists AND
whether the file it points to actually exists on disk (a DB row with
a missing file is reported as broken, not verified).

Writes a JSON + CSV report and prints a summary. Read-only — makes no
DB changes.
"""
import csv
import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from content.models import Question, PastPaper, QuestionImage


STRONG_MARKER = "Diagram/graph"  # covers both "Diagram/graph/structure required" and
                                  # the 2017 paper's "Diagram/graph required" variant

WEAK_KEYWORDS = [
    "figure",
    "diagram",
    "graph",
    "shown below",
    "shown in the figure",
    "shown in figure",
    "structure of",
    "structural formula",
    "truth table",
    "wave figure",
    "following structure",
    "image",
]


class Command(BaseCommand):
    help = "Audit all MDCAT past papers for questions needing an image that don't verifiably have one."

    def add_arguments(self, parser):
        parser.add_argument("--output", default="mdcat-content/verification/image_audit")

    def handle(self, *args, **opts):
        out_base = Path(settings.BASE_DIR) / opts["output"]
        out_base.parent.mkdir(parents=True, exist_ok=True)

        questions = (
            Question.objects.select_related(
                "past_paper", "subtopic__topic__subject"
            )
            .prefetch_related("images")
            .order_by("past_paper__year", "id")
        )

        rows = []
        seen_image_files = {}  # abs path (lowercased) -> [question ids]

        for q in questions:
            text = q.question_text or ""
            lower = text.lower()

            has_strong = STRONG_MARKER in text
            matched_weak = [k for k in WEAK_KEYWORDS if k in lower]
            is_candidate = has_strong or bool(matched_weak) or q.is_visual_required

            if not is_candidate:
                continue

            image_rows = list(q.images.all())
            verified_images = []
            broken_images = []
            for img in image_rows:
                try:
                    p = Path(img.image.path)
                except ValueError:
                    broken_images.append({"id": img.id, "name": img.image.name, "reason": "no file associated"})
                    continue
                if p.exists():
                    verified_images.append({"id": img.id, "name": img.image.name})
                    key = str(p.resolve()).lower()
                    seen_image_files.setdefault(key, []).append(q.id)
                else:
                    broken_images.append({"id": img.id, "name": img.image.name, "reason": "file missing on disk"})

            subject = (
                q.subtopic.topic.subject.name
                if q.subtopic and q.subtopic.topic and q.subtopic.topic.subject
                else ""
            )
            topic = q.subtopic.topic.name if q.subtopic and q.subtopic.topic else ""

            rows.append(
                {
                    "question_id": q.id,
                    "year": q.past_paper.year if q.past_paper else None,
                    "paper": q.past_paper.name if q.past_paper else "",
                    "subject": subject,
                    "topic": topic,
                    "is_verified": q.is_verified,
                    "is_visual_required": q.is_visual_required,
                    "signal": "strong" if has_strong else "weak",
                    "matched_keywords": matched_weak,
                    "verified_image_count": len(verified_images),
                    "broken_image_count": len(broken_images),
                    "verified_images": verified_images,
                    "broken_images": broken_images,
                    "resolved": len(verified_images) > 0,
                    "question_text": text,
                }
            )

        # duplicate image files referenced by more than one question
        duplicates = {k: v for k, v in seen_image_files.items() if len(v) > 1}

        json_path = out_base.with_suffix(".json")
        json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

        csv_path = out_base.with_suffix(".csv")
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "question_id", "year", "paper", "subject", "topic", "is_verified",
                "is_visual_required", "signal", "matched_keywords",
                "verified_image_count", "broken_image_count", "resolved",
            ])
            for r in rows:
                writer.writerow([
                    r["question_id"], r["year"], r["paper"], r["subject"], r["topic"],
                    r["is_verified"], r["is_visual_required"], r["signal"],
                    "|".join(r["matched_keywords"]), r["verified_image_count"],
                    r["broken_image_count"], r["resolved"],
                ])

        # --- summary ---
        by_year = {}
        for r in rows:
            y = r["year"]
            by_year.setdefault(y, {"total": 0, "strong": 0, "resolved": 0, "broken": 0})
            by_year[y]["total"] += 1
            if r["signal"] == "strong":
                by_year[y]["strong"] += 1
            if r["resolved"]:
                by_year[y]["resolved"] += 1
            if r["broken_image_count"] > 0:
                by_year[y]["broken"] += 1

        self.stdout.write(self.style.SUCCESS(f"Wrote {json_path} and {csv_path}"))
        self.stdout.write("")
        self.stdout.write(f"{'Year':<6}{'Candidates':<12}{'Strong':<9}{'Resolved':<10}{'Broken':<8}")
        for y in sorted(by_year, key=lambda v: (v is None, v)):
            s = by_year[y]
            self.stdout.write(f"{str(y):<6}{s['total']:<12}{s['strong']:<9}{s['resolved']:<10}{s['broken']:<8}")

        self.stdout.write("")
        self.stdout.write(f"Total candidates: {len(rows)}")
        self.stdout.write(f"Duplicate image files (used by >1 question): {len(duplicates)}")
        if duplicates:
            for k, v in duplicates.items():
                self.stdout.write(self.style.WARNING(f"  {k} -> questions {v}"))
