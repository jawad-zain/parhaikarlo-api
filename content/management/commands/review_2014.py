from pathlib import Path
from html import escape
import webbrowser

from django.core.management.base import BaseCommand
from content.models import Question, PastPaper


class Command(BaseCommand):
    help = "Open an interactive HTML review page for MDCAT 2014 questions."

    def handle(self, *args, **options):
        try:
            paper = PastPaper.objects.get(exam__slug="mdcat", year=2014)
        except PastPaper.DoesNotExist:
            self.stderr.write(self.style.ERROR("MDCAT 2014 past paper was not found."))
            return

        questions = list(
            Question.objects.filter(past_paper=paper)
            .select_related("subtopic__topic__subject")
            .prefetch_related("images")
            .order_by("id")
        )

        total = len(questions)
        verified = sum(q.is_verified for q in questions)
        unverified = total - verified
        visual_count = sum(q.is_visual_required for q in questions)
        visual_with_image = sum(
            q.is_visual_required and q.images.exists() for q in questions
        )

        rows = []
        for index, q in enumerate(questions, start=1):
            subject = (
                q.subtopic.topic.subject.name
                if q.subtopic and q.subtopic.topic and q.subtopic.topic.subject
                else "Unknown"
            )
            topic = q.subtopic.topic.name if q.subtopic and q.subtopic.topic else "Unassigned"
            status = "verified" if q.is_verified else "unverified"
            visual = "visual" if q.is_visual_required else "non-visual"

            images_html = ""
            for image in q.images.all():
                try:
                    image_uri = Path(image.image.path).resolve().as_uri()
                    images_html += f'''<div class="image-box"><img src="{image_uri}" alt="Question {index} image"></div>'''
                except (ValueError, OSError):
                    images_html += '<div class="image-missing">Image path could not be resolved.</div>'

            searchable = escape(" ".join([
                q.question_text or "",
                q.option_a or "",
                q.option_b or "",
                q.option_c or "",
                q.option_d or "",
                subject,
                topic,
                str(q.id),
            ]))

            rows.append(f'''
<article class="question {status}" data-subject="{escape(subject)}" data-status="{status}" data-visual="{visual}" data-search="{searchable}">
  <div class="question-header">
    <div><span class="question-number">Q{index}</span><span class="database-id">DB ID {q.id}</span></div>
    <div class="status-wrap">
      <span class="status-badge">{"VERIFIED" if q.is_verified else "UNVERIFIED"}</span>
      {f'<span class="visual-badge">VISUAL</span>' if q.is_visual_required else ''}
    </div>
  </div>
  <div class="meta">{escape(subject)} · {escape(topic)}</div>
  <div class="question-text">{escape(q.question_text or "")}</div>
  {images_html}
  <div class="options">
    <div class="option"><span class="option-letter">A</span><span>{escape(q.option_a or "")}</span></div>
    <div class="option"><span class="option-letter">B</span><span>{escape(q.option_b or "")}</span></div>
    <div class="option"><span class="option-letter">C</span><span>{escape(q.option_c or "")}</span></div>
    <div class="option"><span class="option-letter">D</span><span>{escape(q.option_d or "")}</span></div>
  </div>
  <div class="answer"><span>Stored correct answer</span><strong>{escape(q.correct_answer or "—")}</strong></div>
</article>''')

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MDCAT 2014 — Question Review</title>
<style>
:root{{--bg:#0b1020;--panel:#121a2f;--line:rgba(237,230,210,.11);--cream:#ede6d2;--muted:#94a0b4;--gold:#c89b3c;--green:#6b8f71;--green-text:#a6c7aa;--red:#8d3342;--red-text:#e39aa4}}
*{{box-sizing:border-box}} body{{margin:0;background:radial-gradient(circle at 82% 0%,rgba(200,155,60,.10),transparent 28%),var(--bg);color:var(--cream);font-family:Inter,system-ui,sans-serif}}
.container{{max-width:1180px;margin:auto;padding:24px 18px 80px}}
.header{{position:sticky;top:12px;z-index:30;padding:20px;margin-bottom:16px;background:rgba(18,26,47,.96);border:1px solid var(--line);border-radius:18px;backdrop-filter:blur(14px);box-shadow:0 12px 35px rgba(0,0,0,.18)}}
.brand-row{{display:flex;justify-content:space-between;align-items:flex-start;gap:16px}} h1{{margin:0;font:500 34px Georgia,serif}} .subtitle{{margin-top:7px;color:var(--muted);font-size:12px;line-height:1.55}}
.paper-badge{{padding:7px 10px;border:1px solid rgba(200,155,60,.25);border-radius:999px;color:var(--gold);background:rgba(200,155,60,.08);font-size:10px;font-weight:800;letter-spacing:.08em}}
.summary{{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;margin-top:16px}} .stat{{padding:10px 11px;border:1px solid var(--line);border-radius:10px;background:rgba(255,255,255,.025)}} .stat strong{{display:block;font-size:16px}} .stat span{{display:block;margin-top:3px;color:var(--muted);font-size:9px;text-transform:uppercase;letter-spacing:.07em}} .verified strong{{color:var(--green-text)}} .unverified strong{{color:var(--red-text)}} .image strong{{color:var(--gold)}}
.filters{{display:grid;gap:11px;margin-top:17px;padding-top:15px;border-top:1px solid rgba(237,230,210,.07)}} .filter-group{{display:flex;align-items:center;flex-wrap:wrap;gap:6px}} .filter-label{{width:72px;color:var(--muted);font-size:9px;text-transform:uppercase;letter-spacing:.09em}}
.filter,.clear-btn{{border:1px solid var(--line);background:rgba(255,255,255,.025);color:#aeb7c6;padding:7px 10px;border-radius:8px;font-size:10px;cursor:pointer}} .filter:hover,.clear-btn:hover{{border-color:rgba(200,155,60,.34);color:var(--cream)}} .filter.active{{background:rgba(200,155,60,.12);border-color:rgba(200,155,60,.34);color:var(--gold)}}
.search-row{{display:flex;gap:8px;align-items:center}} .search{{width:100%;max-width:520px;padding:10px 12px;border:1px solid var(--line);border-radius:9px;background:rgba(255,255,255,.025);color:var(--cream);outline:none;font-size:12px}} .search:focus{{border-color:rgba(200,155,60,.42)}} .results-count{{margin-top:9px;color:var(--muted);font-size:10px}}
.question-list{{display:grid;gap:13px}} .question{{padding:18px;background:var(--panel);border:1px solid var(--line);border-radius:16px}} .question.unverified{{border-color:rgba(141,51,66,.34)}} .question.hidden{{display:none}}
.question-header{{display:flex;justify-content:space-between;align-items:center;gap:12px}} .question-number{{color:var(--gold);font:18px Georgia,serif}} .database-id{{margin-left:8px;color:#66738a;font:10px monospace}} .status-wrap{{display:flex;align-items:center;gap:6px}}
.status-badge,.visual-badge{{padding:5px 8px;border-radius:999px;font-size:8px;font-weight:800;letter-spacing:.08em}} .verified .status-badge{{color:var(--green-text);background:rgba(107,143,113,.12);border:1px solid rgba(107,143,113,.22)}} .unverified .status-badge{{color:var(--red-text);background:rgba(141,51,66,.16);border:1px solid rgba(141,51,66,.24)}} .visual-badge{{color:#b8c8de;background:rgba(111,143,184,.10);border:1px solid rgba(111,143,184,.18)}}
.meta{{margin-top:9px;color:var(--gold);font-size:9px;letter-spacing:.08em;text-transform:uppercase}} .question-text{{margin-top:12px;color:var(--cream);font-size:15px;line-height:1.65;white-space:pre-wrap}}
.options{{display:grid;gap:7px;margin-top:15px}} .option{{display:flex;gap:10px;padding:10px 12px;border:1px solid rgba(237,230,210,.08);border-radius:9px;background:rgba(255,255,255,.025);color:#b9c1ce;font-size:12px;line-height:1.55}} .option-letter{{flex:0 0 auto;color:var(--gold);font:800 12px monospace}}
.image-box{{margin-top:15px;padding:10px;border:1px solid rgba(237,230,210,.08);border-radius:10px;background:#090f1f;text-align:center}} .image-box img{{max-width:100%;max-height:580px;border-radius:7px}} .image-missing{{margin-top:15px;padding:10px 12px;border-radius:9px;background:rgba(141,51,66,.12);color:var(--red-text);font-size:11px}}
.answer{{display:flex;align-items:center;gap:7px;margin-top:14px;padding:10px 12px;border-left:3px solid var(--gold);border-radius:8px;background:rgba(200,155,60,.07);color:var(--muted);font-size:11px}} .answer strong{{color:var(--gold);font-size:14px}}
@media(max-width:900px){{.summary{{grid-template-columns:repeat(3,minmax(0,1fr))}}}} @media(max-width:620px){{.container{{padding:14px 10px 50px}}.brand-row{{flex-direction:column}}h1{{font-size:29px}}.summary{{grid-template-columns:repeat(2,minmax(0,1fr))}}.filter-label{{width:100%}}.search-row{{flex-direction:column;align-items:stretch}}.search{{max-width:none}}}}
</style>
</head>
<body>
<div class="container">
<header class="header">
  <div class="brand-row">
    <div><h1>MDCAT 2014 — Question Review</h1><div class="subtitle">Review stored answer keys and verification status before finalizing this past paper.</div></div>
    <div class="paper-badge">CONTENT REVIEW</div>
  </div>
  <div class="summary">
    <div class="stat"><strong>{total}</strong><span>Total questions</span></div>
    <div class="stat verified"><strong>{verified}</strong><span>Verified</span></div>
    <div class="stat unverified"><strong>{unverified}</strong><span>Remaining</span></div>
    <div class="stat"><strong>{visual_count}</strong><span>Visual</span></div>
    <div class="stat image"><strong>{visual_with_image}</strong><span>Visual with image</span></div>
  </div>
  <div class="filters">
    <div class="filter-group"><span class="filter-label">Subject</span>
      <button class="filter active" data-filter-type="subject" data-value="all">All</button>
      <button class="filter" data-filter-type="subject" data-value="Biology">Biology</button>
      <button class="filter" data-filter-type="subject" data-value="Chemistry">Chemistry</button>
      <button class="filter" data-filter-type="subject" data-value="Physics">Physics</button>
      <button class="filter" data-filter-type="subject" data-value="English">English</button>
      <button class="filter" data-filter-type="subject" data-value="Logical Reasoning">Logical Reasoning</button>
    </div>
    <div class="filter-group"><span class="filter-label">Status</span>
      <button class="filter active" data-filter-type="status" data-value="all">All</button>
      <button class="filter" data-filter-type="status" data-value="verified">Verified</button>
      <button class="filter" data-filter-type="status" data-value="unverified">Unverified</button>
    </div>
    <div class="filter-group"><span class="filter-label">Visual</span>
      <button class="filter active" data-filter-type="visual" data-value="all">All</button>
      <button class="filter" data-filter-type="visual" data-value="visual">Visual</button>
      <button class="filter" data-filter-type="visual" data-value="non-visual">Non-visual</button>
    </div>
    <div class="search-row"><input id="search" class="search" type="search" placeholder="Search question, option, topic, or DB ID..."><button id="clearFilters" class="clear-btn">Clear</button></div>
    <div id="resultsCount" class="results-count"></div>
  </div>
</header>
<main class="question-list">{"".join(rows)}</main>
</div>
<script>
const state={{subject:"all",status:"all",visual:"all"}};
const questions=Array.from(document.querySelectorAll(".question"));
const searchInput=document.getElementById("search");
const resultsCount=document.getElementById("resultsCount");
function applyFilters(){{const query=searchInput.value.toLowerCase().trim();let visible=0;questions.forEach(q=>{{const matchSubject=state.subject==="all"||q.dataset.subject===state.subject;const matchStatus=state.status==="all"||q.dataset.status===state.status;const matchVisual=state.visual==="all"||q.dataset.visual===state.visual;const search=(q.dataset.search||"").toLowerCase();const matchSearch=!query||search.includes(query)||q.innerText.toLowerCase().includes(query);const show=matchSubject&&matchStatus&&matchVisual&&matchSearch;q.classList.toggle("hidden",!show);if(show)visible++;}});resultsCount.textContent=`Showing ${{visible}} of ${{questions.length}} questions`;}}
document.querySelectorAll(".filter").forEach(button=>{{button.addEventListener("click",()=>{{const type=button.dataset.filterType;state[type]=button.dataset.value;document.querySelectorAll(`.filter[data-filter-type="${{type}}"]`).forEach(b=>b.classList.remove("active"));button.classList.add("active");applyFilters();}});}});
searchInput.addEventListener("input",applyFilters);
document.getElementById("clearFilters").addEventListener("click",()=>{{state.subject="all";state.status="all";state.visual="all";searchInput.value="";document.querySelectorAll(".filter").forEach(b=>b.classList.toggle("active",b.dataset.value==="all"));applyFilters();}});
applyFilters();
</script>
</body>
</html>'''

        output = Path.cwd() / "mdcat_2014_review.html"
        output.write_text(html, encoding="utf-8")
        webbrowser.open_new_tab(output.resolve().as_uri())
        self.stdout.write(self.style.SUCCESS(f"Opened MDCAT 2014 review: {output}"))