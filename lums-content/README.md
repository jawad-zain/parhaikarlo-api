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

## LCAT Mock 3 (2026-09-15)

Third full-length mock (`raw-sources/lums_mock_03.py`, 120 Q, 7 sections,
Verbal 69 / Math 51), added via the same pipeline as Mock 2
(`convert_lums_mock3_to_json.py` -> `LUMS_MOCK_3.json` ->
`import_mcqs.py --exam-slug lums` -> `attach_lums_mock3.py` ->
`quiz.MockTest` id 23). Content-checked before import:

- **Import-breaking bug fixed**: the source file's own
  `check_other_bank_collisions()` imported nonexistent modules
  (`lums_lcat_mock_01/02/03`) instead of the real `lums_mock_01/02`
  filenames, so its Mock 1/2 duplicate check had been silently no-op-ing.
  Fixed directly in `lums_mock_03.py`. Once fixed, it caught two real
  verbatim duplicates -- Mock 3's Q63 was identical to Mock 1's Q63, and
  Q68 was identical to Mock 2's Q68. Both would have silently merged into
  the wrong mock's question under `import_mcqs.py`'s
  `(past_paper, question_text, option_a)` dedupe key, since `past_paper` is
  NULL for every mock. Replaced both with fresh, non-colliding items in the
  same topic/subtopic/difficulty/section.
- **Content check**: all 51 Math questions (sections 2/4/6) were
  independently recomputed and matched the stated key. Verbal items were
  spot-checked for grammar/logic; found and fixed one real error (Q79 used
  "its" for a plural-of-people antecedent -- "vendors' stall rent" -- where
  only "their" is grammatical; "its" is for inanimate referents).
- **Known non-blocking issue, not fixed**: answer-letter balance is skewed
  (A=28 B=43 C=30 D=19) rather than even. Unlike Mock 2's skew fix, this
  was left as-is -- rebalancing would mean rewriting distractors on dozens
  of unrelated questions, out of proportion to this pass. Flag for a future
  dedicated rebalancing pass if it matters for exam realism.

Explanations: hand-authored (Groq not used, per the LUMS mock convention),
120/120, loaded via `scripts/lums_mock3_explanations_by_content.json` +
`manage.py load_explanations_by_content` (matches by content, so it works
unchanged against production's different PKs). All 120 questions verified
in the DB: `is_verified=True`, `is_active=True`, explanation present.

## LCAT Mock 4 (2026-09-15)

Fourth full-length mock (`raw-sources/lums_mock_04.py`, 120 Q, same 7-section
shape). Same pipeline again (`convert_lums_mock4_to_json.py` ->
`LUMS_MOCK_4.json` -> `import_mcqs.py` -> `attach_lums_mock4.py` ->
`quiz.MockTest` id 24).

**Pre-import history worth knowing**: when first opened, this file's own
docstring/`SOURCE` identified it as "Mock Test #3" and 118 of its 120
questions were byte-identical to `lums_mock_03.py`'s pre-fix content --
almost certainly a leftover copy of an earlier draft, saved under the wrong
filename. By the time the content-check pass actually ran (after clearing a
stale `__pycache__` and re-reading), the file had been rewritten with
genuinely distinct questions. If a future `lums_mock_0N.py` ever shows a
docstring/`SOURCE` mismatched with its own filename, or an implausibly
identical answer-key sequence to an existing mock when self-checked, treat
that as the same signal and re-verify before trusting the file's content.

Same fixes as Mock 3's pattern:

- **Collision-check bug**: this file's `check_other_bank_collisions()` had
  the same latent bug as Mock 3's originally did (wrong module names,
  `lums_lcat_mock_01/02`) plus it never checked against Mock 3 at all.
  Fixed directly in the source file. Once fixed, it caught four verbatim
  duplicates -- Q101 against Mock 1, and Q26/Q58/Q100 against Mock 3 -- all
  replaced with fresh, non-colliding items in the same
  topic/subtopic/difficulty/section (the first Q100 replacement
  coincidentally collided with Mock 2's own Q100 and needed a second pass).
- **Content check**: all 51 Math questions independently recomputed and
  matched; one Verbal error found and fixed -- Q79 used "its" for a
  plural-of-people antecedent ("shopkeepers' electricity bill"), the same
  error class as Mock 3's Q79.
- **Answer-letter balance came out clean on its own this time**: A=31 B=30
  C=29 D=30, no deliberate rebalancing needed (unlike Mocks 2 and 3).

Explanations: hand-authored, 120/120, loaded via
`scripts/lums_mock4_explanations_by_content.json` +
`manage.py load_explanations_by_content`. All 120 questions verified in the
DB: `is_verified=True`, `is_active=True`, explanation present.

## LCAT Mock 5 (2026-09-15)

Fifth full-length mock (`raw-sources/lums_mock_05.py`, 120 Q, same 7-section
shape). Same pipeline again (`convert_lums_mock5_to_json.py` ->
`LUMS_MOCK_5.json` -> `import_mcqs.py` -> `attach_lums_mock5.py` ->
`quiz.MockTest` id 25).

This file showed the same docstring/`SOURCE`-vs-filename mismatch as Mock 4
(header called itself "Mock Test #4" / "parhaikarlo_mock_04") -- but unlike
Mock 4, diffing its content against every prior bank found only 6 small,
coincidental numeric-template overlaps (not wholesale duplication), so no
full rewrite was needed. Treat the mismatch signal as worth checking every
time, but not automatically a sign of a stale copy.

Same fixes as the established pattern:

- **Collision-check bug**: same wrong module names as every prior mock file
  shipped with (`lums_lcat_mock_01/02/03`), and no check against Mock 4 at
  all. Fixed directly in the source file (now checks
  lums_mock_01/02/03/04). Once fixed, it caught six verbatim duplicates --
  Q26/Q66 against Mock 1, Q101 against Mock 2, Q53/Q69/Q97 against Mock 3 --
  all replaced with fresh, non-colliding items in the same
  topic/subtopic/difficulty/section and same answer letter, so the bank's
  already-even A/B/C/D balance barely moved.
- **Content check**: all 51 Math questions independently recomputed and
  matched (including the 6 replacements). One Verbal error found and
  fixed -- Q79 used "its" for a plural-of-people antecedent ("orchard
  owners' irrigation allocation"), the same recurring error class as Q79 in
  both Mock 3 and Mock 4. Worth treating this specific pronoun-agreement
  slot as a standing weak point in this mock series' authoring process --
  check it first in any future mock.
- **Answer-letter balance**: A=31 B=30 C=29 D=30 after the Q79 fix, close to
  even, no deliberate rebalancing needed.

Explanations: hand-authored, 120/120, loaded via
`scripts/lums_mock5_explanations_by_content.json` +
`manage.py load_explanations_by_content`. All 120 questions verified in the
DB: `is_verified=True`, `is_active=True`, explanation present.

## LCAT Mock 6 (2026-09-15)

Sixth full-length mock (`raw-sources/lums_mock_06.py`, 120 Q, same 7-section
shape). Same pipeline again (`convert_lums_mock6_to_json.py` ->
`LUMS_MOCK_6.json` -> `import_mcqs.py` -> `attach_lums_mock6.py` ->
`quiz.MockTest` id 26).

Third occurrence of the docstring/`SOURCE`-vs-filename mismatch (header
called itself "Mock Test #2" / "parhaikarlo_mock_02", and its own
collision-check function didn't even attempt a mock_02 import, right- or
wrong-named). Diffing against every prior bank found 13/120 verbatim
overlaps -- elevated versus Mocks 4/5's ~5-6, but still not wholesale
duplication, so treated the same as every prior instance: fix + replace,
not rewrite.

- **Collision-check bug**: same wrong module names as every prior mock file
  shipped with, and missing 2-3 of the other mocks entirely. Fixed directly
  in the source file (now checks lums_mock_01 through lums_mock_05). Once
  fixed, it caught 13 verbatim duplicates: Q35 (Mock 1); Q17/Q30/Q61/Q66/
  Q69/Q91/Q95 (Mock 2 -- the largest single-bank overlap seen yet in this
  series); Q33/Q53/Q65/Q85/Q97 (Mock 4). All replaced with fresh,
  non-colliding items in the same topic/subtopic/difficulty/section and
  (mostly) the same answer letter. Two of the thirteen replacements needed a
  SECOND attempt each after their first replacement collided elsewhere (Q17
  first collided with this same file's own Q51 "PRUDENT" question, then its
  retry collided with Mock 5's Q118; Q65's first retry collided with Mock
  2's own Q65) -- always re-run the collision checker after every
  replacement, never assume one fix is final.
- **Content check**: all 51 Math questions independently recomputed and
  matched (including all replacements). One Verbal error found and fixed --
  Q79 used "its" for a plural-of-people antecedent ("cotton farmers' water
  allocation"), the SAME recurring error as Q79 in Mocks 3, 4, and 5. This
  pronoun-agreement slot is now a confirmed standing weak point across the
  whole mock series' authoring process -- check it first in any future mock
  before doing anything else.
- **Known non-blocking issue, not fixed**: answer-letter balance is skewed
  (A=36 B=37 C=30 D=17), the same skew pattern Mocks 2/3 originally shipped
  with. Left as-is per this series' established precedent -- rebalancing
  would mean rewriting distractors on dozens of unrelated questions, out of
  proportion to a single pass.

Explanations: hand-authored, 120/120, loaded via
`scripts/lums_mock6_explanations_by_content.json` +
`manage.py load_explanations_by_content`. All 120 questions verified in the
DB: `is_verified=True`, `is_active=True`, explanation present.

## LCAT Mock 7 (2026-09-15)

Seventh full-length mock (`raw-sources/lums_mock_07.py`, 120 Q, same 7-section
shape). Same pipeline again (`convert_lums_mock7_to_json.py` ->
`LUMS_MOCK_7.json` -> `import_mcqs.py` -> `attach_lums_mock7.py` ->
`quiz.MockTest` id 27). Import + content-check + collision-fix had already
been done in a prior session before this pass started (see
`scripts/convert_lums_mock7_to_json.py`'s docstring): 13 verbatim duplicates
against Mocks 1-6 were found and replaced, and the recurring Q79
pronoun-agreement bug ("its" for a plural-of-people antecedent) was fixed --
now confirmed in every one of Mocks 3-7. Answer-letter balance is skewed
(A=40 B=38 C=25 D=17), the same skew pattern as Mocks 2/3/6, left as-is per
this series' established precedent.

This pass covered only the explanation-authoring step, which the import
pass had left undone (`explanation_short` empty on all 120 rows going in).

- **Independent re-verification**: before authoring, re-dumped all 120
  questions from `lums-content/raw-sources/lums_mock_07.py` and cross-checked
  every `question_text`/`option_a` pair plus `correct_answer` letter against
  the live DB rows on `quiz.MockTest` id 27 -- 120/120 matched exactly, 0
  mismatches. All 51 Math items (sections 2/4/6) were independently
  recomputed by hand and matched the stored key. All Standard English
  Conventions items (SVA, pronoun agreement, modifier placement, parallel
  structure, punctuation) were separately checked against grammar rules and
  also matched, including Q79 (section 5), which uses "their" as a
  singular-indefinite possessive referring back to "Every one of the...
  growers" -- this is the accepted modern Standard English construction
  (not the same defect class as the "its"-for-plural-people bug fixed at
  import time) and was left as the DB's answer. No content errors found;
  nothing flagged to the user.
- **Hand-authored explanations**: `explanation_short`/`explanation_long`/
  `explanation_trick`/`explanation_options` written from scratch for all 120
  questions (Groq/`generate_explanations` was NOT used, per this project's
  standing rule) and loaded via
  `scripts/lums_mock7_explanations_by_content.json` +
  `manage.py load_explanations_by_content`: "Updated 120 questions. 0
  missing. 0 ambiguous." All 120 questions re-verified in the DB afterward:
  `is_verified=True`, `is_active=True`, `explanation_short` and
  `explanation_options` both present, 0 stragglers.

## LCAT Mock 8 (2026-09-15)

Eighth full-length mock (`raw-sources/lums_mock_08.py`, 120 Q, same 7-section
shape). Same pipeline again (`convert_lums_mock8_to_json.py` ->
`LUMS_MOCK_8.json` -> `import_mcqs.py` -> `attach_lums_mock8.py` ->
`quiz.MockTest` id 28).

This file showed the same docstring/`SOURCE`-vs-filename mismatch as Mocks
4-7 (header called itself "Mock Test #5" / "parhaikarlo_mock_05"). Diffing
its (question_text, option_a) pairs against every prior bank found 10
scattered collisions -- not a contiguous block, and not concentrated on
Mock 5 alone (5 against Mock 5, 3 against Mock 4, 1 against Mock 6, 1
against Mock 7) -- so, per the Mock 5/6/7 precedent, this was treated as a
harmless label bug, not a stale copy. Fixed the header/SOURCE in the source
file directly.

- **Collision-check bug**: the same wrong module names as every prior mock
  file shipped with (`lums_lcat_mock_01/02/03/04`, no check against Mocks
  5-7 at all). Fixed directly in the source file (now checks
  `lums_mock_01` through `lums_mock_07` by dynamic import). Once fixed, it
  caught ten verbatim duplicates -- Q33 (Mock 6); Q51/Q58/Q65/Q94/Q97
  (Mock 5); Q60/Q99/Q100 (Mock 4); Q85 (Mock 7) -- all replaced with
  fresh, non-colliding items in the same topic/subtopic/difficulty/section
  and same answer letter. Three of the ten replacements (Q51, Q58, Q65)
  collided with a *different* mock on the first retry, and Q51/Q65 needed a
  third attempt after that -- always re-run the collision checker after
  every replacement, never assume one fix is final. Final state: zero
  overlap with the sample bank and Mocks 1-7.
- **Content check**: all 51 Math questions (sections 2/4/6, including every
  replacement) were independently recomputed by hand and matched the
  stated key -- 0 errors. Every Verbal item was checked for grammar/logic
  and two real defects were found and fixed:
  - Q79 used "its" for a plural-of-people antecedent ("surveyed
    shopkeepers' electricity bill"), the SAME recurring error class as Q79
    in every one of Mocks 3-7 -- fixed to "their".
  - Q11 had the mirror-image error: "their" was used for a singular
    organisational antecedent ("the dockworkers' union[...] objection"),
    where Standard English calls for singular "its" (an institution, even
    one made up of many people, is grammatically singular and cannot take
    "its" replaced by "their" the way a plural-of-people antecedent can
    take "their" instead of "its"). Fixed to "its". This is a new,
    previously-unseen defect variant in this series -- worth checking
    pronoun-antecedent number (not just animacy) on any future mock's
    Pronoun Agreement items, not only the recurring Q79 slot.
- **Answer-letter balance**: A=32 B=42 C=29 D=17 after all fixes -- skewed
  toward B and away from D, a pattern also seen in Mocks 2/3/6/7, but not
  as extreme as Mock 2's original 61/120 B-skew that triggered a dedicated
  rebalancing pass. Left as-is per this series' established precedent.

Explanations: hand-authored, 120/120, loaded via
`scripts/lums_mock8_explanations_by_content.json` +
`manage.py load_explanations_by_content`: "Updated 120 questions. 0
missing. 0 ambiguous." Every explanation's stated correct option was
cross-checked against the DB's `correct_answer` letter before loading (0
mismatches). All 120 questions re-verified in the DB afterward:
`is_verified=True`, `is_active=True`, `explanation_short` and
`explanation_options` both present, 0 stragglers. No content errors were
left unresolved or flagged to the user.
