"""Correct the claims in the "MDCAT Past Papers 2008-2025" blog post.

The post (slug mdcat-past-papers-guide) was written before the answer-key
passes and lives only in the database — no seeder carries its body. It said,
four times, that every answer key was "verified by MDCAT graduates": a
credential nobody can back, and the site-wide wording is now "checked
against the official key — and against the science" (lib/site.ts
ANSWER_CHECK on the frontend). It also said defective questions are "kept
visible but flagged", when they are switched off and named in the paper's
own note, and its year table carried stale counts (2015 as 220, 2024 as 200,
2008-2013 as "~220") and a PMDC-era summary that never mentioned 2025's
drop to 180 MCQs.

The table below is the live per-subject count of active questions on every
MDCAT paper (it sums to 3,360, the figure /past-papers prints).

NOT touched here, on purpose: the "3.5 hours" timing lines. The exam length
is pass 11, which needs PMDC's own notification before anything is written.

Each fix is an exact string swap. Already-applied fixes are skipped, so this
is safe to re-run; if any expected text is missing entirely, nothing is
saved and the script says which.

    python manage.py shell -c "exec(open('scripts/fix_past_papers_guide_copy.py').read())"
"""

from django.db import transaction

from blog.models import Post

SLUG = "mdcat-past-papers-guide"

OLD_TABLE = """| Year | Total MCQs | Subjects | Notes |
|------|-----------|----------|-------|
| 2008 | ~220 | Bio / Chem / Phys / Eng | Older UHS format, no Logical Reasoning section |
| 2009 | ~220 | Bio / Chem / Phys / Eng | Similar structure to 2008 |
| 2010 | ~220 | Bio / Chem / Phys / Eng | Solid coverage of biology fundamentals |
| 2011 | ~220 | Bio / Chem / Phys / Eng | |
| 2012 | ~220 | Bio / Chem / Phys / Eng | |
| 2013 | ~220 | Bio / Chem / Phys / Eng | |
| 2014 | 220 | Bio / Chem / Phys / Eng | Strong genetics and stoichiometry emphasis |
| 2015 | 220 | Bio / Chem / Phys / Eng | Heavier diagram-based physics |
| 2016 | 216 | Bio / Chem / Phys / Eng | |
| 2017 | 216 | Bio 88 / Chem 54 / Phys 44 / Eng 30 | Official UHS Paper Code, clean answer key |
| 2018 | 219 | Bio 88 / Chem 58 / Phys 43 / Eng 30 | Official UHS Paper Code C |
| 2019 | 200 | Bio 80 / Chem 60 / Phys 40 / Eng 20 | Official UHS Paper Code A, transition year |
| 2022 | 200 | Bio 68 / Chem 54 / Phys 54 / Eng 18 / LR 6 | First PMDC-era paper, Logical Reasoning introduced |
| 2023 | 195 | Bio / Chem / Phys / Eng / LR | |
| 2024 | 200 | Bio 68 / Chem 54 / Phys 54 / Eng 18 / LR 6 | Current PMDC weightage locked in |
| 2025 | 180 | Bio / Chem / Phys / Eng / LR | Most recent official paper |"""

NEW_TABLE = """| Year | MCQs on ParhaiKrlo | Subjects | Notes |
|------|-----------|----------|-------|
| 2008 | 216 | Bio 69 / Chem 58 / Phys 60 / Eng 29 | Older UHS format, no Logical Reasoning section |
| 2009 | 213 | Bio 66 / Chem 58 / Phys 59 / Eng 30 | Similar structure to 2008 |
| 2010 | 219 | Bio 70 / Chem 60 / Phys 59 / Eng 30 | Solid coverage of biology fundamentals |
| 2011 | 220 | Bio 88 / Chem 58 / Phys 44 / Eng 30 | |
| 2012 | 219 | Bio 87 / Chem 58 / Phys 44 / Eng 30 | |
| 2013 | 218 | Bio 88 / Chem 58 / Phys 44 / Eng 28 | |
| 2014 | 214 | Bio 88 / Chem 55 / Phys 42 / Eng 29 | Strong genetics and stoichiometry emphasis |
| 2015 | 218 | Bio 87 / Chem 57 / Phys 44 / Eng 30 | Heavier diagram-based physics |
| 2016 | 216 | Bio 87 / Chem 58 / Phys 42 / Eng 29 | |
| 2017 | 216 | Bio 88 / Chem 54 / Phys 44 / Eng 30 | Official UHS Paper Code |
| 2018 | 219 | Bio 88 / Chem 58 / Phys 43 / Eng 30 | Official UHS Paper Code C |
| 2019 | 200 | Bio 80 / Chem 60 / Phys 40 / Eng 20 | Official UHS Paper Code A, last UHS-era paper |
| 2022 | 200 | Bio 68 / Chem 54 / Phys 54 / Eng 18 / LR 6 | First PMDC-era paper, Logical Reasoning introduced |
| 2023 | 195 | Bio 66 / Chem 54 / Phys 53 / Eng 16 / LR 6 | |
| 2024 | 197 | Bio 66 / Chem 53 / Phys 54 / Eng 18 / LR 6 | Last 200-MCQ paper |
| 2025 | 180 | Bio 81 / Chem 45 / Phys 36 / Eng 9 / LR 9 | Most recent paper; same 180-MCQ split as MDCAT 2026 |

Where a year shows fewer MCQs than the paper printed, the missing questions could not be recovered or had no valid answer; each paper's own note on ParhaiKrlo says which ones and why."""

# (field, old, new)
FIXES = [
    ("excerpt",
     "Each paper's answer key has been verified by MDCAT graduates so you can trust every mark.",
     "Every answer is checked against the official key — and against the science — and we say so wherever they disagree."),
    ("meta_description",
     "Every answer key verified by MDCAT graduates.",
     "Answers checked against the official key and the science."),
    ("body",
     "Every paper below has been transcribed, tagged by topic and sub-topic, and had its answer key manually verified by MDCAT graduates. If a question was defective or had no valid option in the original paper, we've marked it as such rather than silently swapping the answer.",
     "Every paper below has been transcribed and tagged by topic and sub-topic, and every answer checked against the official key — and against the science. If a question was defective or had no valid option in the original paper, we've left it out rather than guess an answer."),
    ("body", OLD_TABLE, NEW_TABLE),
    ("body",
     "every answer key here was cross-checked against the official UHS/PMDC key and independently verified by MDCAT graduates. Where the original source had a defective question (missing options, ambiguous phrasing, unresolved diagrams), we've kept the question visible but flagged it rather than fabricating an answer.",
     "every answer here was checked against the official UHS/PMDC key — and against the science. Where the two disagree, we mark the answer the science supports, and that question's explanation says so and why ([how we mark papers](/past-papers#answer-keys)). Where the original source had a defective question (missing options, ambiguous phrasing, unresolved diagrams), we've switched it off rather than fabricating an answer, and the paper's note names it."),
    ("body",
     "Total MCQs settled at 200 with a 3.5-hour window.",
     "Papers ran 200 MCQs from 2022 to 2024; 2025 dropped to 180, the format MDCAT 2026 keeps."),
]

post = Post.objects.filter(slug=SLUG).first()
if post is None:
    print(f"SKIP: no post {SLUG!r} on this database")
else:
    applied, already, missing = 0, 0, []
    for field, old, new in FIXES:
        text = getattr(post, field)
        if new in text:
            already += 1
        elif old in text:
            setattr(post, field, text.replace(old, new))
            applied += 1
        else:
            missing.append(f"{field}: {old[:70]}...")
    if missing:
        print("ABORT — expected text not found, nothing saved:")
        for m in missing:
            print("  ", m)
    elif applied:
        assert len(post.excerpt) <= 300 and len(post.meta_description) <= 160
        with transaction.atomic():
            post.save()
        print(f"OK: {applied} fix(es) applied, {already} already in place")
    else:
        print(f"NO-OP: all {already} fixes already in place")
    leftover = [w for w in ("graduate", "flagged it") if w in (post.body + post.excerpt + post.meta_description)]
    if leftover:
        print("WARNING: still contains", leftover)
