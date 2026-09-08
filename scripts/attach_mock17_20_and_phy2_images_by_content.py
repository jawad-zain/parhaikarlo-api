"""Attach image-question diagrams for mocks 17-20 and the phy_practice2
practice bank by content match, not PK — same pattern as
attach_mock_images_by_content.py (mocks 10-16), extended for the newer files.

Usage (from backend/, venv active):
    python scripts/attach_mock17_20_and_phy2_images_by_content.py
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

MODULES = {
    "mock17": "mdcat_mock17",
    "mock18": "mdcat_mock_18",
    "mock19": "mdcat_mock_19",
    "mock20": "mdcat_mock_20",
    "phy_practice2": "mdcat_phy_practice2",
}


def attach(label, module_name):
    mod = importlib.import_module(module_name)
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
            print(f"  {label} q{q['id']}: NO MATCHING QUESTION in DB")
            continue

        if question.images.exists():
            skipped += 1
            continue

        src = ROOT / "mdcat-content" / img
        if not src.exists():
            missing_file += 1
            print(f"  {label} q{q['id']}: source image missing on disk: {src}")
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

    print(f"{label}: attached={attached} skipped(existing)={skipped} "
          f"missing_question={missing_q} missing_file={missing_file}")


if __name__ == "__main__":
    labels = sys.argv[1:] or list(MODULES)
    for label in labels:
        attach(label, MODULES[label])
