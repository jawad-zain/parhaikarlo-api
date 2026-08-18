"""Import sourced/cropped question images into the DB from a manifest.

Manifest is a JSON list of objects:
  {
    "question_id": 2040,
    "filename": "q2040_forces_meter_rod.png",   # file in --staging-dir
    "note": "Q3"                                 # optional, not stored
  }

For each entry:
  - question must exist
  - source file (staging_dir/filename) must exist
  - skips (does not duplicate) if the question already has a QuestionImage
    pointing at a file that exists on disk, unless --replace-broken is set
    (in which case broken rows -- pointing at missing files -- are removed
    and replaced)
  - copies the file into MEDIA_ROOT/question_images/<filename>
  - creates a QuestionImage row (source_name/source_year from --source-name
    / --source-year)
  - sets question.is_visual_required = True

Dry-run by default; pass --apply to persist changes and copy files.
"""
import json
import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from content.models import Question, QuestionImage


class Command(BaseCommand):
    help = "Import sourced question images (from a JSON manifest) into the DB."

    def add_arguments(self, parser):
        parser.add_argument("manifest", type=str, help="Path to manifest JSON")
        parser.add_argument("--staging-dir", required=True, help="Directory containing the image files named in the manifest")
        parser.add_argument("--source-name", default="MDCAT", help="QuestionImage.source_name")
        parser.add_argument("--source-year", type=int, default=None, help="QuestionImage.source_year")
        parser.add_argument("--apply", action="store_true", help="Actually write changes. Omit for dry-run.")
        parser.add_argument("--replace-broken", action="store_true", help="Replace existing QuestionImage rows whose file is missing on disk")

    def handle(self, *args, **opts):
        manifest_path = Path(opts["manifest"])
        staging_dir = Path(opts["staging_dir"])
        apply = opts["apply"]

        if not manifest_path.exists():
            raise CommandError(f"Manifest not found: {manifest_path}")
        if not staging_dir.exists():
            raise CommandError(f"Staging dir not found: {staging_dir}")

        entries = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.stdout.write(f"Loaded {len(entries)} entries from {manifest_path.name}")
        if not apply:
            self.stdout.write(self.style.WARNING("DRY RUN - no writes, no file copies"))

        dest_dir = Path(settings.MEDIA_ROOT) / "question_images"

        added = skipped_existing = missing_question = missing_file = replaced = 0
        seen_dest_names = set()

        with transaction.atomic():
            for entry in entries:
                qid = entry["question_id"]
                filename = entry["filename"]

                try:
                    q = Question.objects.get(pk=qid)
                except Question.DoesNotExist:
                    missing_question += 1
                    self.stdout.write(self.style.ERROR(f"question {qid}: not found in DB"))
                    continue

                src_path = staging_dir / filename
                if not src_path.exists():
                    missing_file += 1
                    self.stdout.write(self.style.ERROR(f"question {qid}: staged file missing: {src_path}"))
                    continue

                existing_images = list(q.images.all())
                broken = []
                verified = []
                for img in existing_images:
                    try:
                        p = Path(img.image.path)
                    except ValueError:
                        broken.append(img)
                        continue
                    if p.exists():
                        verified.append(img)
                    else:
                        broken.append(img)

                if verified:
                    skipped_existing += 1
                    self.stdout.write(f"question {qid}: already has a verified image, skipping")
                    continue

                if broken and not opts["replace_broken"]:
                    self.stdout.write(self.style.WARNING(
                        f"question {qid}: has {len(broken)} broken image row(s) (file missing) — "
                        f"pass --replace-broken to replace them"
                    ))
                    continue

                dest_name = filename
                if dest_name in seen_dest_names:
                    self.stdout.write(self.style.ERROR(f"question {qid}: duplicate destination filename {dest_name}, skipping"))
                    continue
                seen_dest_names.add(dest_name)

                dest_path = dest_dir / dest_name
                if dest_path.exists():
                    self.stdout.write(self.style.WARNING(f"question {qid}: {dest_path} already exists on disk, will not overwrite"))
                    continue

                self.stdout.write(f"question {qid}: {filename} -> question_images/{dest_name}" + (" (replacing broken row)" if broken else ""))

                if apply:
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_path, dest_path)

                    if broken:
                        for img in broken:
                            img.delete()
                        replaced += len(broken)

                    QuestionImage.objects.create(
                        question=q,
                        image=f"question_images/{dest_name}",
                        source_name=opts["source_name"],
                        source_year=opts["source_year"],
                    )
                    if not q.is_visual_required:
                        q.is_visual_required = True
                        q.save(update_fields=["is_visual_required"])

                added += 1

            if not apply:
                transaction.set_rollback(True)

        mode = "APPLIED" if apply else "DRY-RUN (nothing saved)"
        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(
            f"[{mode}] added={added} skipped_existing={skipped_existing} "
            f"replaced_broken={replaced} missing_question={missing_question} missing_file={missing_file}"
        ))
        if not apply:
            self.stdout.write("Re-run with --apply to persist.")
