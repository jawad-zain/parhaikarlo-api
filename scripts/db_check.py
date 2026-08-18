import sys, os, django
from pathlib import Path

# add project root to path so 'config' and 'content' are importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from content.models import PastPaper, Question

total = Question.objects.count()
print('=== OVERALL ===')
print(f'Total: {total}')
print(f'  tagged: {Question.objects.filter(subtopic__isnull=False).count()}')
print(f'  untagged: {Question.objects.filter(subtopic__isnull=True).count()}')
print(f'  verified: {Question.objects.filter(is_verified=True).count()}')
print(f'  needs review: {Question.objects.filter(is_verified=False).count()}')
print(f'  active: {Question.objects.filter(is_active=True).count()}')
print(f'  inactive: {Question.objects.filter(is_active=False).count()}')
print()
print('=== PER PAPER ===')
for p in PastPaper.objects.order_by('-year'):
    qs = p.questions
    print(f'{p.year}: {qs.count()} Qs | '
          f'verified={qs.filter(is_verified=True).count()} '
          f'needs_review={qs.filter(is_verified=False).count()} | '
          f'active={qs.filter(is_active=True).count()} '
          f'inactive={qs.filter(is_active=False).count()}')