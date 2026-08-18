"""
Django management command to export all active questions as a single self-contained HTML file
for offline verification.

Place at: content/management/commands/export_questions_html.py

Usage:
    python manage.py export_questions_html
    python manage.py export_questions_html --output review.html
    python manage.py export_questions_html --paper 2015
    python manage.py export_questions_html --only-unverified
"""

import base64
import json
import mimetypes
from pathlib import Path
from django.core.management.base import BaseCommand
from content.models import Question


class Command(BaseCommand):
    help = "Export active questions to a single self-contained HTML file for verification"

    def add_arguments(self, parser):
        parser.add_argument("--output", default="review_questions.html")
        parser.add_argument("--paper", type=int, default=None)
        parser.add_argument("--only-unverified", action="store_true")
        parser.add_argument(
            "--only-visual",
            action="store_true",
            help="Export only questions marked as requiring a diagram/image.",
        )
        parser.add_argument("--include-inactive", action="store_true")

    def handle(self, *args, **opts):
        qs = Question.objects.select_related(
            "past_paper", "subtopic__topic__subject"
        )
        if not opts["include_inactive"]:
            qs = qs.filter(is_active=True)
        if opts["only_unverified"]:
            qs = qs.filter(is_verified=False)
        if opts["only_visual"]:
            qs = qs.filter(is_visual_required=True)
        if opts["paper"]:
            qs = qs.filter(past_paper__year=opts["paper"])

        qs = qs.order_by("past_paper__year", "id")
        total = qs.count()
        self.stdout.write(f"Rendering {total} questions...")

        rows = []
        for q in qs.prefetch_related("images"):
            st = q.subtopic
            tp = st.topic if st else None
            sj = tp.subject if tp else None
            images = []
            for question_image in q.images.all():
                try:
                    image_path = Path(question_image.image.path)
                    mime_type = mimetypes.guess_type(image_path.name)[0] or "image/png"
                    images.append(
                        f"data:{mime_type};base64,"
                        f"{base64.b64encode(image_path.read_bytes()).decode('ascii')}"
                    )
                except (OSError, ValueError):
                    # Keep the review export usable if one historical image file is absent.
                    continue

            rows.append({
                "id": q.id,
                "year": q.past_paper.year if q.past_paper else None,
                "subject": sj.name if sj else "",
                "topic": tp.name if tp else "",
                "subtopic": st.name if st else "",
                "text": q.question_text or "",
                "a": q.option_a or "", "b": q.option_b or "",
                "c": q.option_c or "", "d": q.option_d or "",
                "stored": (q.correct_answer or "").upper(),
                "verified": bool(q.is_verified),
                "active": bool(q.is_active),
                "images": images,
            })

        out_path = Path(opts["output"])
        out_path.write_text(render_html(rows), encoding="utf-8")
        self.stdout.write(self.style.SUCCESS(f"Wrote {total} Qs -> {out_path.resolve()}"))


def render_html(rows):
    data_json = json.dumps(rows, ensure_ascii=False)
    return r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>ParhaiKarlo Review</title>
<style>
:root{--bg:#f7f5f0;--panel:#fff;--ink:#1a1a1a;--muted:#6b6b6b;--line:#e5e1d8;--accent:#7a4d2b;--stored:#2d6a4f;--stored-bg:#d8ede0;--flag:#c1440e;--flag-bg:#fbe4d5}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--ink);font-size:15px;line-height:1.5}
header{position:sticky;top:0;z-index:10;background:var(--panel);border-bottom:1px solid var(--line);padding:14px 20px;display:flex;gap:14px;align-items:center;flex-wrap:wrap}
header h1{font-size:16px;margin:0;font-weight:600}
.stats{color:var(--muted);font-size:13px}
header input,header select{padding:6px 10px;border:1px solid var(--line);border-radius:4px;background:#fff;font-size:13px}
header input{min-width:220px}
header button{padding:6px 12px;border:1px solid var(--line);border-radius:4px;background:#fff;cursor:pointer;font-size:13px}
header button:hover{background:var(--bg)}
.export-btn{background:var(--accent);color:#fff;border-color:var(--accent)}
main{max-width:900px;margin:0 auto;padding:20px}
.q{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:16px 18px;margin-bottom:14px}
.q .meta{font-size:12px;color:var(--muted);margin-bottom:8px;display:flex;gap:12px;flex-wrap:wrap}
.q .meta .id{color:var(--accent);font-weight:600;font-family:ui-monospace,monospace}
.q .text{margin-bottom:10px;white-space:pre-wrap}
.q .visual{display:block;max-width:100%;height:auto;margin:12px 0;border:1px solid var(--line);border-radius:6px;background:#fff}
.q .opts{list-style:none;padding:0;margin:0 0 12px 0}
.q .opts li{padding:6px 10px;margin-bottom:4px;border-radius:4px;border:1px solid transparent}
.q .opts li.stored{background:var(--stored-bg);border-color:var(--stored);color:var(--stored);font-weight:500}
.q .opts li .letter{display:inline-block;width:20px;font-weight:600;font-family:ui-monospace,monospace}
.q .actions{display:flex;gap:6px;padding-top:10px;border-top:1px dashed var(--line);flex-wrap:wrap}
.q .actions button{padding:4px 10px;border:1px solid var(--line);border-radius:4px;background:#fff;cursor:pointer;font-size:12px;font-family:ui-monospace,monospace}
.q .actions button:hover{background:var(--bg)}
.q .actions button.picked{background:var(--flag-bg);border-color:var(--flag);color:var(--flag);font-weight:600}
.q .actions .label{font-size:12px;color:var(--muted);margin-right:6px;align-self:center}
.q .actions .verified-btn.on{background:var(--stored-bg);border-color:var(--stored);color:var(--stored)}
.q.done{opacity:.55}
.drawer{position:fixed;bottom:0;left:0;right:0;background:var(--panel);border-top:2px solid var(--accent);padding:12px 20px;max-height:40vh;overflow-y:auto;box-shadow:0 -2px 12px rgba(0,0,0,.08);transform:translateY(100%);transition:transform .2s}
.drawer.open{transform:translateY(0)}
.drawer h3{margin:0 0 8px 0;font-size:14px;display:flex;justify-content:space-between}
.drawer textarea{width:100%;height:140px;font-family:ui-monospace,monospace;font-size:13px;border:1px solid var(--line);border-radius:4px;padding:8px;resize:vertical}
.drawer .btn-row{display:flex;gap:8px;margin-top:8px}
.drawer button{padding:6px 12px;border:1px solid var(--line);border-radius:4px;background:#fff;cursor:pointer;font-size:13px}
.drawer .copy{background:var(--accent);color:#fff;border-color:var(--accent)}
.no-results{text-align:center;color:var(--muted);padding:40px}
</style></head><body>
<header>
<h1>ParhaiKarlo Review</h1>
<span class="stats" id="stats"></span>
<input type="search" id="search" placeholder="Search text / id...">
<select id="year-filter"><option value="">All years</option></select>
<select id="subject-filter"><option value="">All subjects</option></select>
<label style="font-size:13px;"><input type="checkbox" id="hide-done"> Hide reviewed</label>
<button class="export-btn" onclick="toggleDrawer()">Export fixes (<span id="fix-count">0</span>)</button>
</header>
<main id="list"></main>
<div class="drawer" id="drawer">
<h3>Fixes (format: <code>id: LETTER</code>)
<button onclick="toggleDrawer()" style="border:none;background:none;font-size:18px;cursor:pointer;">X</button></h3>
<textarea id="fix-output" readonly></textarea>
<div class="btn-row">
<button class="copy" onclick="copyFixes()">Copy to clipboard</button>
<button onclick="downloadFixes()">Download .txt</button>
<button onclick="clearFixes()" style="color:var(--flag);">Clear all</button>
</div></div>
<script>
const DATA = __DATA__;
const state = {
  fixes: JSON.parse(localStorage.getItem('pk_fixes')||'{}'),
  reviewed: JSON.parse(localStorage.getItem('pk_reviewed')||'{}'),
  hideDone: false,
};
function esc(s){return String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function renderList(){
  const search=document.getElementById('search').value.toLowerCase().trim();
  const yearF=document.getElementById('year-filter').value;
  const subjF=document.getElementById('subject-filter').value;
  const parts=[];let shown=0;
  for(const q of DATA){
    if(yearF && String(q.year)!==yearF)continue;
    if(subjF && q.subject!==subjF)continue;
    if(search){const hay=(q.text+' '+q.a+' '+q.b+' '+q.c+' '+q.d+' '+q.id).toLowerCase();if(!hay.includes(search))continue;}
    const reviewed=state.reviewed[q.id];
    if(state.hideDone && reviewed)continue;
    shown++;
    const stored=q.stored;const picked=state.fixes[q.id];
    const imageHtml=(q.images||[]).map(src=>`<img class="visual" src="${src}" alt="Diagram for question ${q.id}">`).join('');
    const optHtml=['a','b','c','d'].map(k=>{const isStored=stored===k.toUpperCase();return `<li class="${isStored?'stored':''}"><span class="letter">${k.toUpperCase()}.</span> ${esc(q[k])}</li>`;}).join('');
    const btnHtml=['A','B','C','D'].map(letter=>{const on=picked===letter;return `<button class="${on?'picked':''}" onclick="pickFix(${q.id},'${letter}')">${letter}</button>`;}).join('');
    parts.push(`<div class="q ${reviewed?'done':''}" data-id="${q.id}">
      <div class="meta"><span class="id">#${q.id}</span><span>${q.year||'?'}</span><span>${esc(q.subject)}</span>${q.topic?`<span>${esc(q.topic)}</span>`:''}<span>Stored: <strong>${stored||'-'}</strong></span>${q.verified?'<span style="color:var(--stored);">verified</span>':''}</div>
      <div class="text">${esc(q.text)}</div>${imageHtml}<ul class="opts">${optHtml}</ul>
      <div class="actions"><span class="label">Correct is:</span>${btnHtml}
      <button onclick="clearFix(${q.id})" style="margin-left:8px;">match stored</button>
      <button class="verified-btn ${reviewed?'on':''}" onclick="toggleReviewed(${q.id})" style="margin-left:auto;">${reviewed?'reviewed':'mark reviewed'}</button>
      </div></div>`);
  }
  document.getElementById('list').innerHTML=parts.join('')||'<div class="no-results">No questions match.</div>';
  document.getElementById('stats').textContent=`${shown} / ${DATA.length} shown | ${Object.keys(state.fixes).length} flips | ${Object.keys(state.reviewed).length} reviewed`;
  document.getElementById('fix-count').textContent=Object.keys(state.fixes).length;
}
function pickFix(id,letter){const q=DATA.find(x=>x.id===id);if(q && q.stored===letter){delete state.fixes[id];}else{state.fixes[id]=letter;}state.reviewed[id]=true;save();renderList();refreshDrawer();}
function clearFix(id){delete state.fixes[id];state.reviewed[id]=true;save();renderList();refreshDrawer();}
function toggleReviewed(id){if(state.reviewed[id])delete state.reviewed[id];else state.reviewed[id]=true;save();renderList();}
function save(){localStorage.setItem('pk_fixes',JSON.stringify(state.fixes));localStorage.setItem('pk_reviewed',JSON.stringify(state.reviewed));}
function refreshDrawer(){const lines=Object.entries(state.fixes).sort((a,b)=>Number(a[0])-Number(b[0])).map(([id,letter])=>`${id}: ${letter}`);document.getElementById('fix-output').value=lines.join('\n');}
function toggleDrawer(){refreshDrawer();document.getElementById('drawer').classList.toggle('open');}
function copyFixes(){const ta=document.getElementById('fix-output');ta.select();document.execCommand('copy');alert('Copied '+Object.keys(state.fixes).length+' fixes.');}
function downloadFixes(){const blob=new Blob([document.getElementById('fix-output').value],{type:'text/plain'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='fixes.txt';a.click();}
function clearFixes(){if(!confirm('Clear all queued fixes?'))return;state.fixes={};save();renderList();refreshDrawer();}
(function(){const years=[...new Set(DATA.map(q=>q.year).filter(Boolean))].sort();const subjects=[...new Set(DATA.map(q=>q.subject).filter(Boolean))].sort();const ys=document.getElementById('year-filter');const ss=document.getElementById('subject-filter');years.forEach(y=>ys.innerHTML+=`<option value="${y}">${y}</option>`);subjects.forEach(s=>ss.innerHTML+=`<option value="${esc(s)}">${esc(s)}</option>`);})();
document.getElementById('search').addEventListener('input',renderList);
document.getElementById('year-filter').addEventListener('change',renderList);
document.getElementById('subject-filter').addEventListener('change',renderList);
document.getElementById('hide-done').addEventListener('change',e=>{state.hideDone=e.target.checked;renderList();});
renderList();
</script></body></html>
""".replace("__DATA__", data_json)
