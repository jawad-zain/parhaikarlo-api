"""One-off diagnostic: active-question counts broken down by category, to
diff local vs production and find where a total-count gap comes from.

Usage (from backend/, venv active): python scripts/count_active_questions.py
"""
import os
import sys
from pathlib import Path

import django

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from content.models import Question, PastPaper, Subject  # noqa: E402
from quiz.models import MockTest  # noqa: E402

print("=== SiteStatsView numbers (what the homepage shows) ===")
print("total_papers (active):", PastPaper.objects.filter(is_active=True).count())
print("total_questions (active):", Question.objects.filter(is_active=True).count())
print("total_mock_tests (active):", MockTest.objects.filter(is_active=True).count())
print("total_subjects (active):", Subject.objects.filter(is_active=True).count())

print("\n=== breakdown of active questions ===")
mock_ids = set()
for m in MockTest.objects.all():
    mock_ids.update(m.questions.values_list("id", flat=True))

paper_active = Question.objects.filter(is_active=True, past_paper__isnull=False).count()
mock_active = Question.objects.filter(is_active=True, id__in=mock_ids).count()
practice_active = Question.objects.filter(is_active=True, past_paper__isnull=True).exclude(id__in=mock_ids).count()
print("  linked to a PastPaper:", paper_active)
print("  in a MockTest:", mock_active)
print("  standalone practice:", practice_active)
print("  sum:", paper_active + mock_active + practice_active)

print("\n=== per past paper (active / total) ===")
for p in PastPaper.objects.select_related("exam").order_by("exam__name", "year"):
    qs = Question.objects.filter(past_paper=p)
    print(f"  {p.exam} {p.year}: {qs.filter(is_active=True).count()} / {qs.count()}  (paper is_active={p.is_active})")

print("\n=== per mock test (active / total) ===")
for m in MockTest.objects.select_related("exam").order_by("exam__name", "id"):
    qs = m.questions.all()
    print(f"  {m.exam} | {m.name}: {qs.filter(is_active=True).count()} / {qs.count()}  (mock is_active={m.is_active})")

print("\n=== standalone practice, active, by exam/subject ===")
from collections import Counter  # noqa: E402

practice_qs = Question.objects.filter(
    is_active=True, past_paper__isnull=True
).exclude(id__in=mock_ids).select_related("subtopic__topic__subject__exam")
counts = Counter(
    f"{q.subtopic.topic.subject.exam.name} | {q.subtopic.topic.subject.name}"
    for q in practice_qs
)
for k, v in sorted(counts.items()):
    print(f"  {v}  {k}")
print("  total:", sum(counts.values()))
