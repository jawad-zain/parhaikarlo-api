import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from content.models import Question


# These are candidate-detection keywords only.
# They do NOT automatically mark a question as visual-required.
VISUAL_KEYWORDS = [
    "figure",
    "diagram",
    "graph",
    "shown below",
    "shown in the figure",
    "shown in figure",
    "structure of",
    "structural formula",
    "truth table",
    "wave figure",
    "following structure",
    "image",
]


class Command(BaseCommand):
    help = "Generate an HTML review page for possible visual/image-dependent questions."

    def add_arguments(self, parser):
        parser.add_argument(
            "--output",
            default="review_visual_questions.html",
            help="Output HTML filename.",
        )
        parser.add_argument(
            "--all",
            action="store_true",
            help="Include every active verified question instead of only candidates.",
        )

    def handle(self, *args, **options):
        output_name = options["output"]
        include_all = options["all"]

        questions = (
            Question.objects
            .filter(is_active=True, is_verified=True)
            .select_related(
                "subtopic__topic__subject",
                "past_paper",
            )
            .order_by("id")
        )

        rows = []

        for q in questions:
            text = q.question_text or ""
            lower_text = text.lower()

            matched_keywords = [
                keyword
                for keyword in VISUAL_KEYWORDS
                if keyword in lower_text
            ]

            # A question appears in the review page if:
            # - it matches one of our candidate keywords, OR
            # - it has already been manually marked visual.
            is_candidate = bool(matched_keywords) or q.is_visual_required

            if not include_all and not is_candidate:
                continue

            subject = q.subtopic.topic.subject
            topic = q.subtopic.topic
            subtopic = q.subtopic

            rows.append(
                {
                    "id": q.id,
                    "year": q.past_paper.year if q.past_paper else "",
                    "paper": q.past_paper.name if q.past_paper else "",
                    "subject": subject.name,
                    "topic": topic.name,
                    "subtopic": subtopic.name,
                    "text": q.question_text,
                    "a": q.option_a,
                    "b": q.option_b,
                    "c": q.option_c,
                    "d": q.option_d,
                    "correct": q.correct_answer,
                    "is_visual_required": q.is_visual_required,
                    "keywords": matched_keywords,
                }
            )

        html = self.build_html(rows)

        output_path = Path(settings.BASE_DIR) / output_name
        output_path.write_text(html, encoding="utf-8")

        self.stdout.write(
            self.style.SUCCESS(
                f"Generated {len(rows)} questions → {output_path}"
            )
        )

    def build_html(self, rows):
        data_json = json.dumps(
            rows,
            ensure_ascii=False,
        )

        # IMPORTANT:
        # This is intentionally NOT an f-string.
        # That means JavaScript ${...} remains normal JavaScript syntax.
        html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>ParhaiKarlo — Visual Question Review</title>

<style>
:root {
    --bg: #f7f5f0;
    --panel: #ffffff;
    --ink: #1a1a1a;
    --muted: #6b6b6b;
    --line: #e5e1d8;
    --accent: #7a4d2b;

    --yes: #2d6a4f;
    --yes-bg: #d8ede0;

    --no: #c1440e;
    --no-bg: #fbe4d5;

    --candidate: #5b4b8a;
    --candidate-bg: #eee8ff;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Roboto,
        sans-serif;
}

header {
    position: sticky;
    top: 0;
    z-index: 20;

    background: var(--panel);
    border-bottom: 1px solid var(--line);

    padding: 14px 20px;
}

.header-top {
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
}

h1 {
    margin: 0;
    font-size: 18px;
}

.stats {
    color: var(--muted);
    font-size: 13px;
}

.controls {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 12px;
}

input,
select,
button {
    padding: 7px 10px;
    border: 1px solid var(--line);
    border-radius: 5px;
    background: #fff;
    font-size: 13px;
}

button {
    cursor: pointer;
}

button:hover {
    background: #f0eee8;
}

.primary {
    background: var(--accent);
    color: white;
    border-color: var(--accent);
}

.tabs {
    display: flex;
    gap: 4px;
    margin-top: 12px;
    flex-wrap: wrap;
}

.tab {
    border-radius: 5px 5px 0 0;
}

.tab.active {
    background: var(--accent);
    color: white;
    border-color: var(--accent);
}

main {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
}

.q {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 7px;

    padding: 16px 18px;
    margin-bottom: 14px;
}

.q.visual {
    border-left: 5px solid var(--yes);
}

.q.not-visual {
    border-left: 5px solid var(--no);
}

.meta {
    font-size: 12px;
    color: var(--muted);

    display: flex;
    gap: 12px;
    flex-wrap: wrap;

    margin-bottom: 8px;
}

.id {
    color: var(--accent);
    font-family: ui-monospace, monospace;
    font-weight: 700;
}

.text {
    font-size: 15px;
    line-height: 1.6;
    margin-bottom: 12px;
    white-space: pre-wrap;
}

.options {
    margin-bottom: 14px;
}

.option {
    padding: 8px 10px;
    margin-bottom: 5px;

    border-radius: 5px;
    border: 1px solid var(--line);
}

.option.correct {
    background: var(--yes-bg);
    border-color: var(--yes);

    color: var(--yes);
    font-weight: 600;
}

.tags {
    display: flex;
    gap: 5px;
    flex-wrap: wrap;
    margin-bottom: 10px;
}

.tag {
    padding: 3px 7px;
    border-radius: 12px;

    background: var(--candidate-bg);
    color: var(--candidate);

    font-size: 11px;
}

.status {
    display: inline-block;

    padding: 4px 8px;
    border-radius: 12px;

    font-size: 11px;
    font-weight: 600;

    margin-bottom: 12px;
}

.status.yes {
    background: var(--yes-bg);
    color: var(--yes);
}

.status.no {
    background: var(--no-bg);
    color: var(--no);
}

.actions {
    display: flex;
    gap: 7px;
    flex-wrap: wrap;

    padding-top: 12px;
    border-top: 1px dashed var(--line);
}

.yes-btn.active {
    background: var(--yes-bg);
    border-color: var(--yes);
    color: var(--yes);
    font-weight: 700;
}

.no-btn.active {
    background: var(--no-bg);
    border-color: var(--no);
    color: var(--no);
    font-weight: 700;
}

.empty {
    text-align: center;
    color: var(--muted);
    padding: 50px;
}
</style>
</head>

<body>

<header>

    <div class="header-top">
        <h1>ParhaiKarlo — Visual Question Review</h1>
        <span class="stats" id="stats"></span>
    </div>

    <div class="controls">

        <input
            type="search"
            id="search"
            placeholder="Search ID / question / subject..."
        >

        <select id="year-filter">
            <option value="">All years</option>
        </select>

        <select id="subject-filter">
            <option value="">All subjects</option>
        </select>

        <button class="primary" onclick="exportFixes()">
            Export Fixes
        </button>

        <button onclick="clearFixes()">
            Clear Fixes
        </button>

    </div>

    <div class="tabs">

        <button
            class="tab active"
            onclick="setTab('all', this)"
        >
            All Candidates
        </button>

        <button
            class="tab"
            onclick="setTab('marked', this)"
        >
            Marked Visual
        </button>

        <button
            class="tab"
            onclick="setTab('unmarked', this)"
        >
            Not Marked
        </button>

        <button
            class="tab"
            onclick="setTab('reviewed', this)"
        >
            Changed This Session
        </button>

    </div>

</header>

<main id="list"></main>

<script>

const DATA = __DATA_JSON__;

let currentTab = "all";

const fixes = {};

function escapeHtml(value) {
    return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


function setTab(tab, button) {

    currentTab = tab;

    document
        .querySelectorAll(".tab")
        .forEach(btn => btn.classList.remove("active"));

    button.classList.add("active");

    render();
}


function populateFilters() {

    const years = [...new Set(
        DATA
            .map(q => q.year)
            .filter(Boolean)
    )].sort((a, b) => b - a);

    const subjects = [...new Set(
        DATA
            .map(q => q.subject)
            .filter(Boolean)
    )].sort();

    const yearSelect =
        document.getElementById("year-filter");

    years.forEach(year => {

        const option =
            document.createElement("option");

        option.value = year;
        option.textContent = year;

        yearSelect.appendChild(option);
    });


    const subjectSelect =
        document.getElementById("subject-filter");

    subjects.forEach(subject => {

        const option =
            document.createElement("option");

        option.value = subject;
        option.textContent = subject;

        subjectSelect.appendChild(option);
    });
}


function filteredData() {

    const search =
        document
            .getElementById("search")
            .value
            .trim()
            .toLowerCase();

    const year =
        document.getElementById("year-filter").value;

    const subject =
        document.getElementById("subject-filter").value;


    return DATA.filter(q => {

        const currentValue =
            Object.prototype.hasOwnProperty.call(fixes, q.id)
                ? fixes[q.id]
                : q.is_visual_required;


        if (currentTab === "marked" && !currentValue) {
            return false;
        }


        if (currentTab === "unmarked" && currentValue) {
            return false;
        }


        if (
            currentTab === "reviewed" &&
            !Object.prototype.hasOwnProperty.call(fixes, q.id)
        ) {
            return false;
        }


        if (
            year &&
            String(q.year) !== String(year)
        ) {
            return false;
        }


        if (
            subject &&
            q.subject !== subject
        ) {
            return false;
        }


        if (search) {

            const haystack = [
                q.id,
                q.text,
                q.subject,
                q.topic,
                q.subtopic,
                q.paper,
            ]
                .join(" ")
                .toLowerCase();

            if (!haystack.includes(search)) {
                return false;
            }
        }


        return true;
    });
}


function render() {

    const items = filteredData();

    const list = document.getElementById("list");


    if (!items.length) {

        list.innerHTML = `
            <div class="empty">
                No questions found.
            </div>
        `;

        updateStats();

        return;
    }


    list.innerHTML = items.map(q => {

        const currentValue =
            Object.prototype.hasOwnProperty.call(fixes, q.id)
                ? fixes[q.id]
                : q.is_visual_required;


        const statusClass =
            currentValue
                ? "yes"
                : "no";


        const statusText =
            currentValue
                ? "VISUAL REQUIRED"
                : "NORMAL / NOT MARKED";


        const candidateTags =
            q.keywords && q.keywords.length
                ? q.keywords
                    .map(
                        k =>
                            `<span class="tag">${escapeHtml(k)}</span>`
                    )
                    .join("")
                : "";


        const yearHtml =
            q.year
                ? `<span>${escapeHtml(q.year)}</span>`
                : "";


        const paperHtml =
            q.paper
                ? `<span>${escapeHtml(q.paper)}</span>`
                : "";


        return `
            <article
                class="q ${
                    currentValue
                        ? "visual"
                        : "not-visual"
                }"
            >

                <div class="meta">

                    <span class="id">
                        ID ${escapeHtml(q.id)}
                    </span>

                    <span>
                        ${escapeHtml(q.subject)}
                    </span>

                    <span>
                        ${escapeHtml(q.topic)}
                    </span>

                    <span>
                        ${escapeHtml(q.subtopic)}
                    </span>

                    ${yearHtml}

                    ${paperHtml}

                </div>


                <div class="tags">
                    ${candidateTags}
                </div>


                <div class="status ${statusClass}">
                    ${statusText}
                </div>


                <div class="text">
                    ${escapeHtml(q.text)}
                </div>


                <div class="options">

                    <div
                        class="option ${
                            q.correct === "A"
                                ? "correct"
                                : ""
                        }"
                    >
                        <strong>A.</strong>
                        ${escapeHtml(q.a)}
                    </div>


                    <div
                        class="option ${
                            q.correct === "B"
                                ? "correct"
                                : ""
                        }"
                    >
                        <strong>B.</strong>
                        ${escapeHtml(q.b)}
                    </div>


                    <div
                        class="option ${
                            q.correct === "C"
                                ? "correct"
                                : ""
                        }"
                    >
                        <strong>C.</strong>
                        ${escapeHtml(q.c)}
                    </div>


                    <div
                        class="option ${
                            q.correct === "D"
                                ? "correct"
                                : ""
                        }"
                    >
                        <strong>D.</strong>
                        ${escapeHtml(q.d)}
                    </div>

                </div>


                <div class="actions">

                    <button
                        class="yes-btn ${
                            currentValue
                                ? "active"
                                : ""
                        }"
                        onclick="setFix(${q.id}, true)"
                    >
                        YES — VISUAL REQUIRED
                    </button>


                    <button
                        class="no-btn ${
                            !currentValue
                                ? "active"
                                : ""
                        }"
                        onclick="setFix(${q.id}, false)"
                    >
                        NO — NORMAL QUESTION
                    </button>

                </div>

            </article>
        `;

    }).join("");


    updateStats();
}


function setFix(id, value) {

    fixes[id] = value;

    render();
}


function updateStats() {

    const markedVisual =
        DATA.filter(q => {

            return Object.prototype.hasOwnProperty.call(
                fixes,
                q.id
            )
                ? fixes[q.id]
                : q.is_visual_required;

        }).length;


    const changed =
        Object.keys(fixes).length;


    document.getElementById("stats").textContent =
        `${DATA.length} candidates • ` +
        `${markedVisual} visual-required • ` +
        `${changed} changed this session`;
}


function exportFixes() {

    const ids =
        Object.keys(fixes);


    if (!ids.length) {

        alert("No changes made.");

        return;
    }


    const text =
        ids
            .sort(
                (a, b) =>
                    Number(a) - Number(b)
            )
            .map(
                id =>
                    `${id}: ${
                        fixes[id]
                            ? "true"
                            : "false"
                    }`
            )
            .join("\n");


    const blob =
        new Blob(
            [text],
            {
                type:
                    "text/plain;charset=utf-8"
            }
        );


    const url =
        URL.createObjectURL(blob);


    const link =
        document.createElement("a");


    link.href = url;

    link.download =
        "visual_question_fixes.txt";


    document.body.appendChild(link);

    link.click();

    link.remove();


    URL.revokeObjectURL(url);
}


function clearFixes() {

    if (
        !confirm(
            "Clear all changes from this browser session?"
        )
    ) {
        return;
    }


    Object.keys(fixes).forEach(id => {
        delete fixes[id];
    });


    render();
}


document
    .getElementById("search")
    .addEventListener(
        "input",
        render
    );


document
    .getElementById("year-filter")
    .addEventListener(
        "change",
        render
    );


document
    .getElementById("subject-filter")
    .addEventListener(
        "change",
        render
    );


populateFilters();

render();

</script>

</body>
</html>
"""

        return html.replace(
            "__DATA_JSON__",
            data_json,
        )