# LUMS ingest playbook

Second exam vertical on this platform, built on the exact MDCAT architecture
(Exam → Subject → Topic → Subtopic → Question). Nothing in `content/models.py`
changed to add LUMS — see "Schema" below for why.

## What LUMS is, here

**LUMS Common Admission Test (LCAT)** — the current LUMS undergraduate
admission test. It mirrors the Digital SAT's own domain taxonomy for its
Verbal and Math sections (e.g. "Craft and Structure", "Advanced Mathematics"
are official LCAT/College-Board domain names, not something invented for this
repo).

**As of 2026-09-08, the only source material ingested is a 24-question
sample bank** (`raw-sources/lums_lcat_sample.py`), built from LUMS' own
official "Sample Questions for Verbal & Math Sections" guide
(`raw-sources/sample_lcat_2025.pdf`). It is **not** a dated past paper and
**has no official answer key** — the source docstring says so explicitly.
Whoever built the `.py` file worked the answers out from the question
content itself (grammar/logic for Verbal, calculation for Math).

Consequences of that:
- Subject scope is **provisionally Verbal + Math only**. Do not add
  Analytical Reasoning / Physics / Chemistry subjects or topics until a real
  LCAT source document is reviewed showing those sections exist in the
  current test format.

**2026-09-09 update:** the user asked for this bank to go through the same
pipeline MDCAT mock tests get — mock tests also ship with no external answer
key, and are still content-verified by Claude reasoning through every
question by hand, then marked `is_verified=True` if that pass finds zero
errors. Applied the same treatment here: all 24 questions were independently
re-derived (grammar/logic for Verbal, hand-worked calculation for Math)
against the DB's stored `correct_answer`, found zero mismatches, and are now
`is_verified=True`. The bank is also no longer standalone — it's attached to
a real `PastPaper` row (`exam=lums`, `slug=lums-sample-past-paper`,
`name="LUMS Sample Past Paper"`, `is_free=True`) via
`scripts/attach_lums_sample.py` (get_or_create + match by
`(question_text, option_a)`, same pattern as the mock `attach_mockN.py`
scripts — chosen over `import_mcqs.py`'s auto-create-by-year path so the
paper gets the name "LUMS Sample Past Paper" instead of the generic
"LUMS 2025"). All 24 questions also have hand-authored
`explanation_short/long/trick/options` loaded via
`scripts/lums_sample_explanations.json` + `manage.py load_explanations`, per
the MDCAT explanation-generation workflow (Groq NOT used).

## Folder layout

```
lums-content/
├── syllabus/
│   └── lums_syllabus.json       # closed vocab for the Groq tagger (UTF-8-sig, matches PMDC's shape)
├── parsed-mcqs/
│   └── LUMS_LCAT_SAMPLE.json    # importer input — regenerable, gitignored (mirrors MDCAT_*.json)
├── raw-sources/
│   ├── sample_lcat_2025.pdf     # source PDF — gitignored (mirrors mdcat-content's *.pdf rule)
│   └── lums_lcat_sample.py      # hand-typed adapter source — committed
└── README.md                    # this file
```

## Schema

**No changes to `content/models.py`.** The 24-question sample bank is plain
4-option MCQs, no shared-passage Analytical-Reasoning-style blocks, no
5-option items. If a future LUMS source turns up either of those, stop and
raise it before writing an importer for it — those are the two schema
changes the original task brief flagged as plausibly justified (an
`option_e` field, or a `context` field for AR game passages). Everything
else bends to the existing model, not the other way around.

## Ingest pipeline (identical shape to MDCAT)

1. **Adapter**: `scripts/convert_lums_sample_to_json.py` reads
   `raw-sources/lums_lcat_sample.py` → writes
   `parsed-mcqs/LUMS_LCAT_SAMPLE.json`.

   This adapter **skips the Groq tagger** for this particular source, because
   the sample bank already carries LUMS' own correct domain names as its
   `topic` field — running that through the tagger would only risk
   *degrading* already-correct metadata. `subtopic` is set equal to `topic`
   (no finer breakdown exists in a 24-Q sample); once real dated past papers
   arrive, tag those against `lums_syllabus.json` with `tag_topics.py` the
   normal way and split subtopics out properly.

   `needs_review` is forced `True` on every row (see "no official key" above)
   so `import_mcqs.py` lands every question `is_verified=False`.

2. **Seed** (one-time, idempotent): `python manage.py seed_lums` creates the
   `Exam(slug="lums")` row and its two `Subject` rows (Verbal, Math).
   `weight_percent` / `question_count` are left at `0` (unknown) rather than
   extrapolated from a 24-question sample pretending to be a full paper —
   fill these in once a real, full-length, dated LCAT past paper is reviewed.
   Run `--dry-run` first to preview.

3. **Import**: `python manage.py import_mcqs lums-content/parsed-mcqs/LUMS_LCAT_SAMPLE.json --exam-slug lums`
   Auto-creates Topic/Subtopic rows via `get_or_create`. Since `paper_year`
   is `null` for every row, no `PastPaper` gets created — all 24 questions
   land with `past_paper=NULL` (practice-only), exactly like MDCAT's practice
   banks.

4. **Idempotency check** — re-run the same import command immediately after.
   Expect `created=0, updated=24`. If it shows `created=24` again, the
   `(past_paper, question_text, option_a)` dedupe key is broken — stop and
   fix `import_mcqs.py` before doing anything else. (Do not touch the dedupe
   key itself — it's shared with MDCAT and exists specifically to survive the
   "Choose the CORRECT sentence" collision bug from Aug 11.)

5. **Verify**: no LLM cross-check pass makes sense for 24 hand-reasoned
   sample questions with no official key to check against — that's a job for
   human review in Django admin once real past papers with real keys arrive.
   For this sample bank, treat `is_verified=False` as correct and permanent
   until either an official key surfaces or a human manually checks each
   answer and flips the flag in admin.

## Adding paper #2 (a real, dated LCAT past paper)

When a real dated past paper shows up (PDF or `.py` adapter):

1. Confirm its actual section list and per-section question counts before
   doing anything else — do not assume it matches the 24-Q sample bank's 14/10
   split, and do not assume it's still just Verbal + Math.
2. If it introduces a new subject (Analytical Reasoning, Physics, Chemistry),
   extend `lums_syllabus.json` and `seed_lums.py`'s `SUBJECTS` list — ask
   before adding a subject that wasn't in the original scoping conversation.
3. Clone `convert_lums_sample_to_json.py` → `convert_lums_<year>_to_json.py`,
   set `paper_year` to the real year, and — unlike the sample bank — actually
   run `scripts/tag_topics.py` against `lums_syllabus.json` (do NOT skip the
   tagger for real papers; the "already tagged" shortcut only applies because
   the sample bank happened to ship with LUMS' own domain labels attached).
4. Output JSON as `lums-content/parsed-mcqs/LUMS_<YEAR>.json` (matches the
   `MDCAT_<YEAR>.json` convention).
5. `import_mcqs.py` will auto-create the `PastPaper "LUMS <YEAR>"` row this
   time, since `paper_year` will be set. Re-run the idempotency check.
6. Update `Subject.weight_percent` / `question_count` on the real per-paper
   counts once you have a genuine full-length paper to measure from.

Same 20-minute turnaround MDCAT papers get, once this file exists as the map.
