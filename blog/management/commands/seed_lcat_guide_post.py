"""Seeds the pillar LCAT post: /blog/lums-lcat-preparation-guide-2026.

Idempotent — re-running updates the existing row in place (matched on slug)
rather than creating a duplicate. `published_at` is only stamped once, by
Post.save(), so a re-run never moves the post's publish date.

Sourcing rules followed here (same bar as the MDCAT posts):

* Every claim about the LCAT's own format comes from LUMS' official
  "Sample Questions for Verbal & Math Sections" guide, a copy of which is in
  this repo at `lums-content/raw-sources/sample_lcat_2025.pdf`. The four
  Verbal and four Math domain descriptions are quoted from it verbatim, and
  they match `lums-content/syllabus/lums_syllabus.json` exactly.
* Every date comes from LUMS' own admissions calendar
  (admission.lums.edu.pk/critical-dates-all-programmes), which as of
  2026-09-12 still showed the Fall 2026 cycle. The post says so explicitly
  instead of guessing at Fall 2027 dates.
* Things LUMS does NOT publish — per-section question counts, per-section
  timing, negative marking, the score scale — are named as unpublished
  rather than filled in from coaching-site numbers that contradict each
  other. Same "flag the gap, never fabricate" rule the past papers post
  follows.
* The 8 full-length LCAT mocks are live in the DB as of 2026-09 and are
  advertised here (linked from /mocks/lums). No dated LCAT past paper is
  implied though — see lib/officialSamples.ts on the frontend for why that
  distinction is load-bearing; the mocks are ParhaiKrlo-authored practice
  tests, not a released LUMS paper.

The body deliberately has no "## FAQs" heading. The frontend injects the
FAQ block (from Post.faqs, as both visible <details> and FAQPage JSON-LD)
immediately before the LAST H2 in the body, so "Practice with ParhaiKrlo"
is kept last and the FAQs land just above it.
"""

from django.core.management.base import BaseCommand

from blog.models import Post

SLUG = 'lums-lcat-preparation-guide-2026'

TITLE = 'LUMS LCAT: Complete Preparation Guide 2026'

EXCERPT = (
    "What LUMS officially publishes about the LCAT and what it doesn't: all eight Verbal and Math "
    "content domains, how the test compares to the SAT, MDCAT and ECAT, the real admission timeline, "
    "and 30, 60 and 90-day study plans."
)

META_TITLE = 'LUMS LCAT Preparation Guide 2026 — Pattern, Syllabus, Timeline'

META_DESCRIPTION = (
    "Complete LCAT guide — official Verbal and Math domains, exam pattern, LUMS admission "
    "timeline and 30/60/90-day study plans. Practise LUMS' official sample."
)

BODY = """\
If you are aiming for LUMS, the LCAT is the one piece of your application you can still move. Your \
grades are largely written by now and your extracurriculars are what they are. The admission test is \
the variable still under your control, and it is the one most applicants prepare for badly — because \
almost everything written about the LCAT online is guesswork dressed up as fact.

This guide is built from LUMS' own published material: the official *Sample Questions for Verbal & \
Math Sections* guide, and the official admissions calendar. Where LUMS publishes something, it is \
quoted. Where LUMS does not — and there is more of that than you would expect — this guide says so \
rather than repeating a number a coaching site invented.

## What is the LCAT?

**LCAT stands for the LUMS Common Admission Test.** It is the Lahore University of Management \
Sciences' own undergraduate admission test, used across all four of its schools: the Suleman Dawood \
School of Business, the Syed Babar Ali School of Science and Engineering, the Mushtaq Ahmad Gurmani \
School of Humanities and Social Sciences, and the Shaikh Ahmad Hassan School of Law.

The most misunderstood fact about it is this: **the LCAT is not compulsory.** LUMS' admission FAQ \
states that applicants must take *one* admission test to be considered, and lists three acceptable \
options — the SAT, the ACT, or the LCAT. The LCAT is simply the option built for applicants inside \
Pakistan: administered locally, far cheaper than an international sitting, and scheduled to fit the \
LUMS application cycle rather than the College Board's.

**Who takes it.** Anyone applying for LUMS undergraduate admission who is not submitting an SAT or \
ACT score — A-Level, FSc, IB and equivalent students, from science and arts backgrounds alike. That \
last part matters more than it sounds. The LCAT contains **no subject-specific content at all**: no \
biology, no chemistry, no physics, no Pakistan Studies. A humanities student is not at a \
disadvantage against a pre-engineering student, because neither is being tested on what they studied \
in college.

**What it is modelled on.** LUMS is unusually direct here. Its official sample guide says: *"The \
LCAT is a multiple-choice test like the SAT. However, the time duration and test format may vary \
from the SAT."* That is not a vague family resemblance — the eight content domains LUMS publishes \
are the Digital SAT's own domain names, in the SAT's own taxonomy.

Which gives you the single most useful fact in this guide: **SAT preparation material is LCAT \
preparation material.** LUMS' own guide tells you to use it, recommending SAT practice tests and \
Khan Academy by name.

## LCAT vs SAT vs MDCAT vs ECAT

Pakistani students routinely conflate these four, and the confusion costs real preparation time. \
Someone who has spent two months on MDCAT-style rote recall walks into the LCAT badly calibrated.

| | **LCAT** | **SAT** | **MDCAT** | **ECAT** |
|---|---|---|---|---|
| Run by | LUMS | College Board | PMDC | UET Lahore |
| Used for | LUMS undergraduate admission | International and LUMS admission | Medical and dental colleges | Engineering universities |
| What it tests | Verbal and Math reasoning | Reading, Writing and Math reasoning | Biology, Chemistry, Physics, English, Logical Reasoning | Physics, Chemistry, Maths, English |
| Subject knowledge needed | None | None | Yes, full FSc syllabus | Yes, full FSc syllabus |
| Format | Paper-based MCQ, four options | Digital, adaptive | Paper-based MCQ, OMR | Paper-based MCQ |
| Duration | Approximately 3 hours | 2 hours 14 minutes | 3 hours | 100 minutes |
| Questions | Not officially published | 98 | 180 | 100 |
| Scoring | Not officially published | 400–1600 | 180 marks, 55% to pass for medical | 400 marks |
| Calculator | Not allowed | Allowed in Math | Not allowed | Not allowed |
| Negative marking | Not officially stated | None | None | None for the 2026 sitting |

**Where the LCAT sits.** It is the only one of the four that examines no school subject. MDCAT and \
ECAT are curriculum exams, rewarding a student who has memorised the PMDC or UET syllabus. The LCAT \
and SAT are aptitude exams, rewarding a student who reads quickly and accurately and can manipulate \
algebra without a calculator. There is no syllabus to finish, only skills to sharpen — which is why \
**LCAT preparation compresses in a way MDCAT preparation never does.**

If you are weighing MDCAT alongside a LUMS application, our [MDCAT preparation hub](/exams/mdcat) \
and the [MDCAT 2026 syllabus guide](/blog/mdcat-2026-syllabus) cover that side separately.

## LCAT Exam Pattern

The honest answer to "what is the LCAT pattern?" is that LUMS publishes some of it and not the rest.

**What LUMS officially confirms,** from the official sample questions guide:

- **Total duration: approximately 3 hours.**
- The test is **multiple choice**, with four options labelled (A), (B), (C) and (D).
- You **fill circles on an answer sheet** — so it is paper-based with OMR marking, not a \
computer-adaptive test like the current digital SAT.
- There are **Verbal sections and Math sections**, both plural.
- **Calculators are not allowed** at any point.
- There are **eight content domains**, four Verbal and four Math, listed in full below.
- You must bring **a printed, signed Test Registration Slip** and **a photo-bearing valid CNIC, \
government-issued juvenile card, or passport.** LUMS states outright that applicants without both \
will not be allowed to take the LCAT. No other identity document is accepted.

**What LUMS does not publish:** the number of questions, the questions per section, the time allowed \
per section, whether there is negative marking, and how raw answers convert into a reported score.

You will find sites that state these confidently. They contradict each other — one widely cited page \
says four sections of 40 minutes, another says seven sections of 25 minutes, and neither cites LUMS. \
Do not build a pacing strategy on either. **Build it on the three-hour total and the eight domains,** \
which are the parts LUMS actually stands behind.

> **The calculator ban matters more than the timing question.** Three hours is generous for a \
reasoning test; doing every percentage, ratio and quadratic by hand is what eats it. Practise \
arithmetic on paper from day one. Students who prepare on a calculator lose marks to slips, not to \
ignorance.

## Verbal Section Breakdown

LUMS describes the Verbal sections as combining "elements of both reading and writing." The four \
domains below use LUMS' official names and official descriptions.

### Craft and Structure

LUMS: this domain *"assess[es] comprehension, vocabulary, and reasoning skills needed to understand \
and use high-utility words, evaluate texts rhetorically, and make connections between related \
texts."*

- **Words in context.** A passage with a blank and four candidate words. You are not asked which \
word you know, but which word the surrounding logic demands. LUMS' sample opens with exactly this: a \
travelogue about Pakistan's regions, where all three wrong options smuggle in a judgement the \
passage never makes.
- **Text structure and purpose.** Why is this paragraph here — what is the author *doing*, as \
opposed to saying?
- **Cross-text connections.** Two short passages, and how the second relates to the first.

**How to prepare:** stop memorising vocabulary lists. High-utility words in context are learned by \
reading dense non-fiction and noticing how precise writers choose between near-synonyms.

### Information and Ideas

LUMS: this domain *"measure[s] the ability to locate, interpret, evaluate, and integrate information \
from texts and informational graphics such as tables and graphs."*

Read that last clause carefully — **there are tables and graphs in the Verbal section.** Students who \
file "charts" under Math get ambushed. The question types:

- **Central ideas and details**, and **inferences** — what must be true given the passage.
- **Command of evidence, textual** — which quotation best supports a claim.
- **Command of evidence, quantitative** — which data point from a table or graph does.
- **Synthesising multiple observations** — three or four bullet-point research notes, and which \
single sentence best combines them for a stated purpose. LUMS' sample uses notes on the Pakistani \
artist Sadequain for this.

**How to prepare:** synthesis questions are the most teachable, because the right answer always \
serves the *stated goal* in the stem rather than merely the facts. Read the goal before the options.

### Standard English Conventions

LUMS: this domain *"test[s] editing skills to ensure texts conform to the core conventions of \
standard English sentence structure, usage, and punctuation."*

This is the highest-return domain on the test, and almost nobody treats it that way. The rule set is \
finite: sentence boundaries (comma splices, run-ons, fragments), subject-verb agreement across \
intervening phrases, pronoun agreement and reference, punctuation, modifier placement, and parallel \
structure.

**How to prepare:** six rules, each with a testable pattern. A motivated student can go from \
unreliable to near-perfect here in about a week. If your diagnostic is weak anywhere, start here — \
nothing else on the LCAT converts study hours into marks this fast.

### Expression of Ideas

LUMS: this domain *"evaluate[s] the ability to revise texts for clarity, effectiveness, and \
rhetorical goals."*

- **Transitions.** Two ideas and four candidate connectives. LUMS' sample has a clean example: \
technological advances improved life quality, *and* produced medical breakthroughs. That is \
consequence, so "Consequently" is right and "Nevertheless" is a trap for anyone picking by ear.
- **Rhetorical synthesis.** Given notes and a specific goal, choose the sentence that achieves it.

**How to prepare:** name the logical relationship in your head *before* reading the options. Picking \
by which word sounds right is the commonest way strong readers lose easy marks.

## Math Section Breakdown

LUMS' own preparation note names the ground: *"focus on mastering algebra, linear equations, \
logarithms, inequalities, data interpretation, ratios, percentages, as well as advanced mathematical \
concepts like quadratic and exponential functions... Since calculators are not allowed, practise \
accuracy in manual calculations."*

Nothing there goes beyond an FSc or A-Level AS mathematics syllabus. The difficulty is speed and \
accuracy under a clock, not depth.

### Algebra

LUMS: *"assesses the ability to analyze, solve, and construct linear equations and inequalities. It \
includes solving equations and systems of equations using various techniques and understanding \
linear functions in one and two variables."*

Linear equations in one and two variables, linear functions, systems, inequalities, arithmetic \
sequences. The most predictable domain on the test — and the most punishing if you are slow, because \
algebra also turns up inside questions from the other three domains. Work for fluency, not just \
correctness: a two-variable system should take under a minute by hand.

### Advanced Mathematics

LUMS: *"evaluates understanding of advanced equations, including absolute value, quadratic, \
exponential, polynomial, rational, and radical equations. It also encompasses working with nonlinear \
functions and solving systems of nonlinear equations."*

Quadratics, nonlinear functions, exponents and radicals, logarithms, polynomial and rational \
expressions. LUMS' sample opens its Math section with a profit function of the form *P(x) = x² − 3x \
+ 2* and asks for the break-even point — a quadratic dressed as a word problem, which is the house \
style. Factorise on sight, and know when the formula beats factoring.

### Problem-Solving and Data Analysis

LUMS: *"measures quantitative reasoning skills in ratios, rates, percentages, and proportional \
relationships. It involves analyzing and interpreting data through statistical models, scatterplots, \
probability concepts, and evaluating claims based on sample statistics."*

Ratios and rates, percentages, unit conversion, weighted averages, table and graph interpretation, \
probability, and basic statistics. This is where the calculator ban bites hardest: percentage-change \
chains and weighted averages are easy to understand and easy to fumble by hand. Drill them until \
they are mechanical.

### Geometry and Trigonometry

LUMS: *"focuses on concepts related to area, volume, angles, triangles, circles, and trigonometric \
functions. It includes solving problems involving properties of shapes, right triangles, and \
trigonometric calculations."*

Area and perimeter, volume and surface area, angles and triangles, Pythagoras, circles including \
arcs and sectors, trigonometric ratios and basic identities. Memorise the special right triangles — \
3-4-5, 5-12-13, 30-60-90, 45-45-90 — because they turn multi-step calculation into recall, which is \
exactly what you want with no calculator.

## LUMS Admission Timeline 2026

**Verification status, stated plainly:** as of 12 September 2026, LUMS' official admissions calendar \
still displays the **Fall 2026** cycle. The Fall 2027 calendar has not been published. Anyone showing \
you confirmed Fall 2027 LCAT dates today is inventing them.

Here is the Fall 2026 cycle exactly as LUMS published it. These dates have passed, but they are the \
template — LUMS has run this same calendar shape for years.

| Milestone | Fall 2026 date |
|---|---|
| Undergraduate online application deadline | Tuesday, 27 January 2026, 5:00 pm PKT |
| Deadline to upload documents and pay the application fee | Wednesday, 28 January 2026 |
| **LUMS Common Admission Test (LCAT)** | **Sunday, 15 February 2026** |
| Financial aid application and documents deadline | Saturday, 28 February 2026 |
| Deadline to take the SAT (if using SAT instead) | Saturday, 14 March 2026 |
| Deadline to take the ACT (if using ACT instead) | Saturday, 11 April 2026 |
| Admission decisions released | 15 April 2026 – 31 July 2026 |

Three things fall out of that calendar which matter more than the exact dates:

1. **The application closes before the test.** You apply in late January and sit the LCAT in \
mid-February. The LCAT is not something you register for after deciding you did well enough.
2. **The SAT deadline is a month after the LCAT.** That is a real safety net: a February LCAT that \
goes badly can still be followed by a March SAT sitting inside the same cycle. Most applicants never \
notice this option exists.
3. **Decisions run to end of July,** overlapping the MDCAT and ECAT cycles entirely. Plan to hold two \
processes open at once.

**On the fee.** The LCAT registration fee is widely reported as PKR 6,500. LUMS' own FAQ refers to \
an "Application Processing and LUMS Test Registration (if applicable) Fee payment voucher" without \
publishing the amount, so treat 6,500 as indicative and confirm it on the voucher your application \
generates.

**If you are reading this in late 2026,** work on applications closing in the last week of January \
2027 and the LCAT sitting around mid-February 2027 — then confirm against admission.lums.edu.pk, not \
against any third-party date including this one, once LUMS publishes the Fall 2027 calendar.

## How to Prepare for LCAT

**Start with a diagnostic, always.** Before any plan, sit a set of real LCAT-style questions cold and \
untimed, then score yourself *by domain*. You are not looking for a total. You are looking for which \
of the eight domains is weakest, because everything below is about directing time where it converts.

### The 90-day track

- **Weeks 1–2 — diagnose, then fix grammar.** Standard English Conventions alone: six rules, drilled \
to reliability. Fastest score movement available anywhere on the test.
- **Weeks 3–6 — build the Math base.** Algebra and Problem-Solving and Data Analysis, worked entirely \
by hand. No calculator from day one.
- **Weeks 7–9 — Verbal reading depth.** Craft and Structure plus Information and Ideas. Read one \
dense non-fiction article daily and write a one-sentence summary of its argument; this trains \
central-idea questions better than any question bank.
- **Weeks 10–11 — Advanced Mathematics and Geometry.** Quadratics, logs, circles, trigonometric \
ratios.
- **Week 12 — full-length timed practice.** Three hours, paper only, no calculator, no phone. At \
least two sittings.
- **Final week — mistake log review only.** No new material.

### The 60-day track

- **Weeks 1–2 — diagnostic plus Standard English Conventions.** Non-negotiable in every track.
- **Weeks 3–5 — Algebra and Problem-Solving and Data Analysis,** by hand.
- **Weeks 6–7 — Verbal reading, plus Expression of Ideas.** Transitions and rhetorical synthesis are \
both quick wins.
- **Week 8 — Geometry essentials and two full timed papers.** Advanced Mathematics gets less time \
than it deserves here; cover quadratics and logs only.

### The 30-day track

Late, but not lost — precisely because the LCAT tests no syllabus.

- **Days 1–3 — diagnostic and triage.** Name your two weakest domains; everything else gets \
maintenance only.
- **Days 4–10 — Standard English Conventions, exclusively.** Still the highest return per hour.
- **Days 11–20 — your two weakest domains.**
- **Days 21–26 — mixed practice under time,** in 40-minute blocks.
- **Days 27–29 — two full three-hour papers,** reviewing every error.
- **Day 30 — rest.** Print and sign your Test Registration Slip, put your CNIC in the bag, and stop.

## Common Mistakes LCAT Aspirants Make

**Preparing for it like MDCAT.** The most expensive mistake here. There is no syllabus to finish and \
nothing to memorise; hours spent making notes are hours not spent doing questions.

**Skipping the grammar domain.** Standard English Conventions is rule-based and completely learnable. \
Students skip it because it feels less impressive than reading comprehension, then lose marks on \
subject-verb agreement.

**Practising with a calculator.** LUMS states the ban explicitly. Every hour of calculator-assisted \
Math practice is an hour that does not transfer.

**Trusting unofficial section timings.** The confident per-section breakdowns online contradict each \
other and cite nothing. Pace against the three-hour total.

**Assuming the LCAT is compulsory.** It is one of three accepted tests, and the SAT deadline falls a \
month after the LCAT date.

**Treating vocabulary as a list.** Words-in-context questions test which word the passage's logic \
requires. Memorised definitions do not answer them.

**Freezing on charts in the Verbal section.** Tables and graphs appear there by design.

**Applying without reading the calendar.** The application closes before the test date, so "decide \
about the test later" is not an option the timeline offers.

**Never sitting a full three-hour paper.** Stamina is a skill, and test day is a poor place to \
discover you do not have it.

**Leaving blanks.** LUMS does not state that there is negative marking. Absent a published penalty, \
a blank is guaranteed to score nothing while a guess is not.

## Practice with ParhaiKrlo

There is no such thing as a dated LCAT past paper — LUMS does not publicly release year-wise LCAT \
papers, which is exactly why so much unreliable information fills the gap. What LUMS *has* released \
is its official sample question set, and that is on ParhaiKrlo.

Every question from it sits on the [LUMS preparation hub](/exams/lums), tagged to the same eight \
official domains this guide walks through, so you can see at a glance where your errors cluster. \
Each question carries an **AI explanation**: get one wrong, and you can pull up why the correct \
answer works, why the option you picked was built to catch you, and which domain the concept belongs \
to — without waiting on a tutor.

Once the domains stop being the problem, the thing to practise is the three-hour sitting itself. \
ParhaiKrlo has 8 full-length [LCAT mock tests](/mocks/lums), timed and weighted the same way across \
Verbal and Math, with instant scoring and an explanation on every question. That is where "Never \
sitting a full three-hour paper" above gets fixed.

If you are also preparing for MDCAT, the [MDCAT hub](/exams/mdcat) has verified [past \
papers](/past-papers) going back to 2008, the full [PMDC syllabus \
breakdown](/blog/mdcat-2026-syllabus), and timed [mock tests](/mocks).

Start with the sample paper, untimed. Score yourself by domain, not by total. Then pick the track \
above that matches the time you actually have left.
"""

FAQS = [
    {
        'question': 'Is the LCAT hard?',
        'answer': (
            "It is demanding in a different way to MDCAT or ECAT rather than harder overall. Nothing on "
            "the LCAT goes beyond an FSc or A-Level AS mathematics syllabus, and there is no subject "
            "content to memorise at all. The difficulty is speed and accuracy under a clock, made "
            "sharper by the fact that calculators are not allowed at any point in the test."
        ),
    },
    {
        'question': 'Is the LCAT compulsory for LUMS admission?',
        'answer': (
            "No. LUMS' admission FAQ states that applicants must take one admission test to be "
            "considered, and lists three acceptable options: the SAT, the ACT, or the LCAT. The LCAT is "
            "the option built for applicants inside Pakistan, administered locally by LUMS and "
            "scheduled to fit the LUMS application cycle."
        ),
    },
    {
        'question': 'Can I retake the LCAT?',
        'answer': (
            "LUMS does not publish a retake policy on its public admission FAQ, so treat the LCAT as a "
            "single sitting within one admission cycle and confirm with the LUMS admissions office if "
            "you need certainty. What the published calendar does give you is a real fallback: the "
            "deadline to take the SAT falls about a month after the LCAT date, so a disappointing LCAT "
            "can still be followed by an SAT sitting inside the same cycle."
        ),
    },
    {
        'question': "What's a good LCAT score?",
        'answer': (
            "LUMS does not publish the LCAT score scale, a passing mark, or year-wise cutoffs, so any "
            "specific number quoted online is invented. LUMS also states there is no minimum score "
            "required for the SAT or ACT, which suggests admission is assessed on the whole application "
            "rather than a test threshold. Aim to maximise your score rather than to clear a cutoff "
            "that has never been published."
        ),
    },
    {
        'question': 'How many questions are on the LCAT and how long is it?',
        'answer': (
            "LUMS officially confirms a total duration of approximately 3 hours, a multiple-choice "
            "format with four options labelled A to D, and both Verbal and Math sections. It does not "
            "publish the number of questions, the questions per section, or the time per section. Sites "
            "that state these confidently contradict each other, so pace your practice against the "
            "three-hour total instead."
        ),
    },
    {
        'question': 'Is there negative marking on the LCAT?',
        'answer': (
            "LUMS does not state in its official materials that the LCAT carries negative marking. "
            "Absent a published penalty, an unanswered question is guaranteed to score nothing while a "
            "guess is not, so never hand back a blank answer sheet."
        ),
    },
    {
        'question': 'Can arts and humanities students take the LCAT?',
        'answer': (
            "Yes, and they are not at a disadvantage. The LCAT contains no subject-specific content: no "
            "biology, chemistry, physics or Pakistan Studies. It tests reading, writing and mathematical "
            "reasoning only, so a humanities student and a pre-engineering student are examined on "
            "exactly the same skills."
        ),
    },
    {
        'question': 'Can I use SAT material to prepare for the LCAT?',
        'answer': (
            "Yes, and LUMS recommends it directly — its official guide tells test takers to review SAT "
            "practice tests and points to Khan Academy by name. The eight LCAT content domains are the "
            "Digital SAT's own domain names, so SAT material maps onto the LCAT almost exactly. The one "
            "adjustment is working without a calculator, since the LCAT does not allow one and the SAT "
            "does."
        ),
    },
    {
        'question': 'When is the LCAT held and when do applications close?',
        'answer': (
            "For the Fall 2026 cycle, LUMS' official calendar set the undergraduate application deadline "
            "at 27 January 2026 and the LCAT at 15 February 2026, with admission decisions released "
            "between 15 April and 31 July 2026. As of 12 September 2026 the Fall 2027 calendar had not "
            "been published, so expect a similar shape and confirm on admission.lums.edu.pk once LUMS "
            "publishes it."
        ),
    },
    {
        'question': 'Are there LCAT past papers?',
        'answer': (
            "No. LUMS does not publicly release year-wise LCAT past papers, which is a large part of why "
            "so much unreliable information about the test circulates. What LUMS has released is an "
            "official sample question set covering both the Verbal and Math sections, and that sample is "
            "on ParhaiKrlo, tagged to the eight official content domains with AI explanations on every "
            "question. ParhaiKrlo also has 8 full-length LCAT mock tests, built to the same pattern, for "
            "timed practice beyond the official sample."
        ),
    },
]


class Command(BaseCommand):
    help = 'Creates or updates the pillar LCAT preparation guide blog post.'

    def handle(self, *args, **options):
        post, created = Post.objects.update_or_create(
            slug=SLUG,
            defaults={
                'title': TITLE,
                'post_type': 'blog',
                'excerpt': EXCERPT,
                'body': BODY,
                'meta_title': META_TITLE,
                'meta_description': META_DESCRIPTION,
                'author_name': 'ParhaiKrlo Team',
                'faqs': FAQS,
                'is_published': True,
            },
        )
        verb = 'Created' if created else 'Updated'
        self.stdout.write(self.style.SUCCESS(
            f'{verb} post /blog/{post.slug} - {len(BODY.split())} body tokens, '
            f'{len(FAQS)} FAQs, published_at={post.published_at}'
        ))
