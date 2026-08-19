"""Import tagged MCQ JSON into Question model."""
import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils.text import slugify

from content.models import Exam, Subject, Topic, Subtopic, PastPaper, Question


class Command(BaseCommand):
    help = "Import tagged MCQs from JSON into the Question model."

    def add_arguments(self, parser):
        parser.add_argument("json_path", type=str)
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--exam-slug", default="mdcat")

    def handle(self, *args, **opts):
        json_path = Path(opts["json_path"])
        if not json_path.exists():
            raise CommandError(f"File not found: {json_path}")

        data = json.loads(json_path.read_text(encoding="utf-8-sig"))
        self.stdout.write(f"Loaded {len(data)} MCQs from {json_path.name}")

        try:
            exam = Exam.objects.get(slug=opts["exam_slug"])
        except Exam.DoesNotExist:
            raise CommandError(f"Exam '{opts['exam_slug']}' not found.")

        subject_cache = {}
        topic_cache = {}
        subtopic_cache = {}
        paper_cache = {}
        created = updated = skipped = errors = review_flagged = 0

        if opts["dry_run"]:
            self.stdout.write(self.style.WARNING("DRY RUN - no writes"))

        with transaction.atomic():
            for mcq in data:
                try:
                    # --- validation gates ---
                    if not mcq.get("correct_answer"):
                        skipped += 1
                        continue
                    if len(mcq.get("options", {}) or {}) != 4:
                        skipped += 1
                        continue
                    if not mcq.get("subject") or not mcq.get("topic") or not mcq.get("subtopic"):
                        skipped += 1
                        continue

                    # --- resolve subject ---
                    subj_name = mcq["subject"]
                    if subj_name not in subject_cache:
                        try:
                            subject_cache[subj_name] = Subject.objects.get(exam=exam, name=subj_name)
                        except Subject.DoesNotExist:
                            raise CommandError(f"Subject '{subj_name}' not seeded.")
                    subject = subject_cache[subj_name]

                    # --- resolve/create topic ---
                    topic_key = (subject.id, mcq["topic"])
                    if topic_key not in topic_cache:
                        topic, _ = Topic.objects.get_or_create(
                            subject=subject,
                            name=mcq["topic"],
                            defaults={"slug": slugify(mcq["topic"])[:150]},
                        )
                        topic_cache[topic_key] = topic
                    topic = topic_cache[topic_key]

                    # --- resolve/create subtopic ---
                    sub_key = (topic.id, mcq["subtopic"])
                    if sub_key not in subtopic_cache:
                        subtopic, _ = Subtopic.objects.get_or_create(
                            topic=topic,
                            name=mcq["subtopic"],
                            defaults={"slug": slugify(mcq["subtopic"])[:150]},
                        )
                        subtopic_cache[sub_key] = subtopic
                    subtopic = subtopic_cache[sub_key]

                    # --- resolve/create past paper ---
                    # paper_year is optional: mock-only questions (not transcribed
                    # from any real past paper) pass paper_year=None/absent and
                    # stay unattached (past_paper=NULL — see Question model docstring).
                    year = mcq.get("paper_year")
                    paper = None
                    if year:
                        if year not in paper_cache:
                            paper, _ = PastPaper.objects.get_or_create(
                                exam=exam,
                                year=year,
                                name=f"{exam.name.upper()} {year}",
                                defaults={"slug": slugify(f"{exam.slug}-{year}"), "is_free": False},
                            )
                            paper_cache[year] = paper
                        paper = paper_cache[year]

                    # --- build field dict ---
                    opts_dict = mcq["options"]
                    is_flagged = bool(mcq.get("needs_review"))
                    if is_flagged:
                        review_flagged += 1

                    q_fields = {
                        "question_text": mcq["question_text"],
                        "option_a": (opts_dict.get("a", "") or "")[:500],
                        "option_b": (opts_dict.get("b", "") or "")[:500],
                        "option_c": (opts_dict.get("c", "") or "")[:500],
                        "option_d": (opts_dict.get("d", "") or "")[:500],
                        "correct_answer": mcq["correct_answer"].upper(),
                        "difficulty": mcq.get("difficulty") or "medium",
                        "explanation_short": "",
                        "explanation_long": "",
                        "explanation_trick": "",
                        "is_active": mcq.get("is_active", True),
                        "is_verified": not is_flagged,
                        "is_visual_required": bool(mcq.get("is_visual_required", False)),
                        "subtopic": subtopic,
                        "past_paper": paper,
                        "paper_order": mcq.get("question_number"),
                    }

                    if opts["dry_run"]:
                        continue

                    # --- dedupe: match on (paper, question_text, option_a) ---
                    # option_a included because MDCAT English section has ~10 Qs per paper
                    # with identical stem "Choose the CORRECT sentence:" — only options differ.
                    existing = Question.objects.filter(
                        past_paper=paper,
                        question_text=q_fields["question_text"],
                        option_a=q_fields["option_a"],
                    ).first()

                    if existing:
                        for k, v in q_fields.items():
                            setattr(existing, k, v)
                        existing.save()
                        updated += 1
                    else:
                        Question.objects.create(**q_fields)
                        created += 1

                except CommandError:
                    raise
                except Exception as e:
                    errors += 1
                    self.stdout.write(self.style.ERROR(f"ERROR on {mcq.get('id')}: {e}"))

            if opts["dry_run"]:
                transaction.set_rollback(True)

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"created: {created}"))
        self.stdout.write(self.style.SUCCESS(f"updated: {updated}"))
        self.stdout.write(f"skipped: {skipped}")
        self.stdout.write(f"flagged for review: {review_flagged}")
        self.stdout.write(f"topics: {len(topic_cache)}, subtopics: {len(subtopic_cache)}")
        if errors:
            self.stdout.write(self.style.ERROR(f"errors: {errors}"))