import django, os, random, html, sys
from pathlib import Path

# add project root to path so 'config' resolves
sys.path.insert(0, str(Path(__file__).parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from content.models import PastPaper, Question

SAMPLE_PER_PAPER = 20
SEED = 42  # change to re-roll a different sample
random.seed(SEED)

out_dir = Path('mdcat-content/spot-checks')
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / 'answer_spot_check.html'

rows = []
for paper in PastPaper.objects.order_by('-year'):
    qs = list(paper.questions.all())
    sample = random.sample(qs, min(SAMPLE_PER_PAPER, len(qs)))
    sample.sort(key=lambda q: q.id)
    for q in sample:
        rows.append((paper.year, q))

def esc(s):
    return html.escape(str(s or ''))

parts = ['''<!doctype html>
<html><head><meta charset="utf-8"><title>MDCAT answer spot-check</title>
<style>
body { font-family: -apple-system, sans-serif; max-width: 780px; margin: 40px auto; padding: 0 20px; color: #222; }
.q { border-bottom: 1px solid #ddd; padding: 20px 0; }
.meta { color: #888; font-size: 13px; font-family: monospace; margin-bottom: 8px; }
.qtext { font-weight: 600; margin-bottom: 10px; }
.opt { padding: 4px 10px; margin: 3px 0; border-radius: 4px; }
.correct { background: #d4edda; border-left: 4px solid #28a745; font-weight: 600; }
.subj { display: inline-block; background: #eee; padding: 2px 8px; border-radius: 3px; font-size: 11px; margin-left: 8px; }
h1 { border-bottom: 2px solid #333; padding-bottom: 8px; }
.summary { background: #fff8dc; padding: 12px 16px; border-radius: 6px; margin-bottom: 20px; }
</style></head><body>
<h1>MDCAT answer spot-check</h1>
<div class="summary">
<b>How to use:</b> read each Q, decide the correct answer yourself, then check the highlighted option.
Note any that look wrong (write Q ID on paper). At the end: &lt;2% wrong = trust source, &gt;5% = do full LLM check.
</div>
''']

for year, q in rows:
    subj = q.subtopic.topic.subject.name if q.subtopic else '?'
    parts.append(f'<div class="q"><div class="meta">MDCAT {year} · Q{q.id}<span class="subj">{esc(subj)}</span></div>')
    parts.append(f'<div class="qtext">{esc(q.question_text)}</div>')
    for letter in ['a', 'b', 'c', 'd']:
        opt_text = getattr(q, f'option_{letter}')
        cls = 'opt correct' if q.correct_answer.lower() == letter else 'opt'
        parts.append(f'<div class="{cls}"><b>{letter.upper()}.</b> {esc(opt_text)}</div>')
    parts.append('</div>')

parts.append('</body></html>')
out_path.write_text('\n'.join(parts), encoding='utf-8')

print(f"Wrote {len(rows)} Qs to {out_path}")
print(f"Papers sampled: {len({y for y, _ in rows})}")
print(f"Open in browser:  start {out_path}")