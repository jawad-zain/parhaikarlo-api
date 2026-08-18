"""Build and open a browser review page for the clean MDCAT 2017 visuals."""

import html
import os
import sys
import webbrowser
from argparse import ArgumentParser
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django  # noqa: E402

django.setup()

from content.models import Question  # noqa: E402


def main():
    parser = ArgumentParser()
    parser.add_argument("--year", type=int, default=2017)
    parser.add_argument("--whole-paper", action="store_true")
    args = parser.parse_args()

    output = PROJECT_ROOT / "media" / (
        f"mdcat_{args.year}_{'full_paper' if args.whole_paper else 'visual_review'}.html"
    )
    questions = Question.objects.filter(past_paper__year=args.year)
    if not args.whole_paper:
        questions = questions.filter(is_visual_required=True, images__isnull=False)
    questions = questions.prefetch_related("images").order_by("paper_order", "id").distinct()
    cards = []
    for question in questions:
        image = question.images.first()
        options = "".join(
            f"<li><strong>{letter}.</strong> {html.escape(option)}</li>"
            for letter, option in zip(
                "ABCD",
                [question.option_a, question.option_b, question.option_c, question.option_d],
            )
        )
        image_html = (
            f'<img src="{html.escape(image.image.name)}" alt="Visual for question {question.id}">'
            if image else ""
        )
        cards.append(
            f"""
            <article>
              <h2>Question {question.paper_order or question.id}</h2>
              <p>{html.escape(question.question_text)}</p>
              {image_html}
              <ol class=\"options\">{options}</ol>
            </article>"""
        )
    output.write_text(
        """<!doctype html><html><head><meta charset=\"utf-8\"><title>MDCAT {year} — Review</title>
        <style>body{margin:0;background:#f4f7fb;font-family:Arial,sans-serif;color:#172033}header{position:sticky;top:0;background:#fff;padding:18px 30px;box-shadow:0 1px 8px #0002;z-index:2}h1{margin:0;font-size:24px}main{max-width:1200px;margin:24px auto;padding:0 18px}article{background:#fff;border-radius:14px;padding:20px;margin:18px 0;box-shadow:0 2px 12px #1231}h2{color:#1867b8;margin:0 0 8px}p{line-height:1.45;white-space:pre-wrap}img{width:100%;height:auto;border:1px solid #d7e0eb;border-radius:10px;margin:10px 0}.options{columns:2;gap:36px;padding-left:24px}.options li{break-inside:avoid;margin:8px 0;padding:8px;background:#f7faff;border-radius:6px}</style>
        </head><body><header><h1>MDCAT {year} — {kind} ({count} questions)</h1></header><main>{cards}</main></body></html>"""
        .replace("{year}", str(args.year))
        .replace("{kind}", "Full paper" if args.whole_paper else "Clean visual review")
        .replace("{count}", str(questions.count()))
        .replace("{cards}", "\n".join(cards)),
        encoding="utf-8",
    )
    print(output)
    webbrowser.open(output.as_uri())


if __name__ == "__main__":
    main()
