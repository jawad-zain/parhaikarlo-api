"""Attach image-question diagrams for mocks 10-16 by content match, not PK.

The existing per-mock image manifests (scripts/mockN_image_manifest.json)
key off a *local* Question.id — useless on a different DB (e.g. production)
where import_mcqs assigns fresh PKs. This script instead re-derives the
match the same way attach_mockN.py does: (question_text, option_a), read
straight from each mock's source .py QUESTIONS list (which still carries
the "image" relative path). Safe to re-run — skips questions that already
have a verified QuestionImage.

Usage (from backend/, venv active):
    python scripts/attach_mock_images_by_content.py 10 11 12 13 14 15 16
    python scripts/attach_mock_images_by_content.py        # all of 10-16
"""
import importlib
import os
import shutil
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "mdcat-content"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.conf import settings
from content.models import Question, QuestionImage

# mock number -> source module name (filenames are inconsistent across mocks —
# some have an underscore before the number, some don't; see mdcat-content/).
MOCK_MODULES = {
    10: "mdcat_mock_10",
    11: "mdcat_mock11",
    12: "mdcat_mock12",
    13: "mdcat_mock13",
    14: "mdcat_mock_14",
    15: "mdcat_mock_15",
    16: "mdcat_mock_16",
}


def attach(n):
    mod = importlib.import_module(MOCK_MODULES[n])
    questions = mod.QUESTIONS

    attached = skipped = missing_q = missing_file = 0
    dest_dir = Path(settings.MEDIA_ROOT) / "question_images"

    for q in questions:
        img = q.get("image")
        if not img:
            continue

        question = Question.objects.filter(
            past_paper__isnull=True,
            question_text=q["question"],
            option_a=q["options"]["A"],
        ).first()
        if not question:
            missing_q += 1
            print(f"  mock {n} q{q['id']}: NO MATCHING QUESTION in DB")
            continue

        if question.images.exists():
            skipped += 1
            continue

        src = ROOT / "mdcat-content" / img
        if not src.exists():
            missing_file += 1
            print(f"  mock {n} q{q['id']}: source image missing on disk: {src}")
            continue

        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_name = src.name
        dest_path = dest_dir / dest_name
        if not dest_path.exists():
            shutil.copy2(src, dest_path)

        QuestionImage.objects.create(
            question=question,
            image=f"question_images/{dest_name}",
            source_name="MDCAT",
        )
        if not question.is_visual_required:
            question.is_visual_required = True
            question.save(update_fields=["is_visual_required"])
        attached += 1

    print(f"Mock {n}: attached={attached} skipped(existing)={skipped} "
          f"missing_question={missing_q} missing_file={missing_file}")


if __name__ == "__main__":
    nums = [int(a) for a in sys.argv[1:]] or list(MOCK_MODULES)
    for n in nums:
        attach(n)
