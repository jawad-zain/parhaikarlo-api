"""Seeds the timely MDCAT post: /blog/mdcat-2026-final-week-revision-plan.

Idempotent — re-running updates the existing row in place (matched on slug)
rather than creating a duplicate. `published_at` is only stamped once, by
Post.save(), so a re-run never moves the post's publish date.

Sourcing rules followed here (same bar as the other pillar posts):

* The exam date, paper pattern, weightage, passing marks and negative-marking
  line are the ones already published in our own MDCAT 2026 syllabus post,
  which was verified against the official PMDC MDCAT curriculum PDF. Nothing
  new about the official pattern is asserted here.
* Every "highest-yield topic" number is counted from this project's own
  database — active, verified past-paper questions for exam MDCAT, papers
  2022-2025 (775 MCQs across four papers), grouped by Topic. The counts were
  produced by a direct ORM aggregation, not estimated. Re-run it with:

      Question.objects.filter(
          past_paper__isnull=False, past_paper__exam__slug='mdcat',
          is_active=True, past_paper__year__gte=2022,
      ).values('subtopic__topic__name').annotate(n=Count('id'))

  If more papers are re-verified the counts will drift; treat the tables in
  BODY as a dated snapshot (stated as such in the post) rather than a
  permanent fact.
* Exam-hall logistics are deliberately hedged to "whatever your roll number
  slip says". PMDC/the conducting university publish the binding list per
  sitting and it is not stable year to year, so the post tells the reader
  where to look instead of inventing a checklist.
* The day-by-day plan is dated Sunday 13 September to Sunday 20 September
  2026 — real weekdays for that calendar, checked, not guessed.
* Platform counts in the CTA (16 papers, 3,363 verified questions, 20 mocks)
  are the live production numbers as of 2026-09-12.

The body has no "## Frequently Asked Questions" heading of its own: the
frontend injects the FAQ block (from Post.faqs, as visible <details> plus
FAQPage JSON-LD) immediately before the LAST H2 in the body, so the closing
CTA section stays last and the FAQs land just above it.
"""

from django.core.management.base import BaseCommand

from blog.models import Post

SLUG = 'mdcat-2026-final-week-revision-plan'

TITLE = 'MDCAT 2026 Final Week: An 8-Day Revision Plan for 20 September'

EXCERPT = (
    "MDCAT 2026 is on Sunday, 20 September. Here is what the last eight days should look like — "
    "a dated day-by-day plan, the highest-yield topics counted from the last four real papers, "
    "and the mistakes that cost marks in the final week."
)

META_TITLE = 'MDCAT 2026 Final Week — 8-Day Revision Plan & Exam Day Guide'

META_DESCRIPTION = (
    "MDCAT 2026 is on 20 September. A dated 8-day revision plan, the highest-yield topics counted "
    "from the 2022-2025 papers, and an exam-day checklist."
)

BODY = """\
MDCAT 2026 is on **Sunday, 20 September 2026**. If you are reading this the week it goes up, you \
have eight days left, and how you spend them is worth more marks than the eight days you spent in \
July. Not because you can learn anything new in eight days, but because this is the window where \
most candidates quietly lose marks they had already earned.

The final week has one job: **convert what you already know into marks on an OMR sheet.** That is a \
different job from learning, and it needs a different plan. Everything below is built on our own \
question-by-question data from the last four real papers, and on the official pattern in our \
[MDCAT 2026 syllabus guide](/blog/mdcat-2026-syllabus).

## The paper you are sitting

| | |
|---|---|
| Date | Sunday, 20 September 2026 |
| Total questions | 180 MCQs |
| Duration | 3 hours (180 minutes) |
| Format | Paper-based, OMR sheet |
| Negative marking | None |
| Passing marks | 55% (99/180) medical, 50% (90/180) dental |

Weightage, as published by PMDC: Biology 81 MCQs, Chemistry 45, Physics 36, English 9, Logical \
Reasoning 9.

Two numbers should shape your week. **Biology and Chemistry are 126 of 180 marks** — 70% of the \
paper. And **there is no negative marking**, which means a blank bubble is a guaranteed zero while a \
guess is a one-in-four chance at a mark. Nobody should leave the hall with an unfilled answer.

Worth knowing: the 2025 paper already ran on exactly this pattern. We counted it — 81 Biology, 45 \
Chemistry, 36 Physics, 9 English, 9 Logical Reasoning, 180 total. The 2026 weightage is not a \
prediction. It is what happened last year.

## What actually gets asked

We hold 16 verified MDCAT past papers. For this post we counted every active, verified question in \
the four most recent ones — 2022, 2023, 2024 and 2025, **775 MCQs in total** — and grouped them by \
PMDC topic. This is the real distribution, not a coaching-centre guess.

**Biology — ten units carry 258 of 283 MCQs (91%)**

| Unit | MCQs, 2022-2025 |
|---|---|
| Biological Molecules | 43 |
| Cell Structure and Function | 41 |
| Coordination and Control | 35 |
| Support and Movement | 33 |
| Reproduction | 26 |
| Inheritance | 19 |
| Enzymes | 17 |
| Evolution | 17 |
| Acellular Life | 14 |
| Bioenergetics | 13 |

**Chemistry — the top ten carry 147 of 207 MCQs (71%)**

| Unit | MCQs, 2022-2025 |
|---|---|
| Chemistry of Hydrocarbons | 24 |
| Chemical Bonding | 21 |
| s and p Block Elements | 18 |
| Chemical Equilibrium | 15 |
| Atomic Structure | 15 |
| Thermochemistry and Energetics | 12 |
| Gases | 12 |
| Solids | 11 |
| Reaction Kinetics | 10 |
| Fundamental Principles of Organic Chemistry | 9 |

Chemistry is the flattest subject on the paper. No unit dominates, which is exactly why blind \
last-week "selective study" hurts here more than anywhere else.

**Physics — the top ten carry 172 of 197 MCQs (87%)**

| Unit | MCQs, 2022-2025 |
|---|---|
| Force and Motion | 26 |
| Work and Energy | 21 |
| Electrostatics | 20 |
| Current Electricity | 20 |
| Electromagnetism | 20 |
| Waves | 19 |
| Rotational and Circular Motion | 14 |
| Nuclear Physics | 13 |
| Electromagnetic Induction | 12 |
| Dawn of Modern Physics | 7 |

**English — one area carries almost all of it.** Of the 61 English MCQs in those four papers, **58 \
tested formal and lexical aspects of language** — grammar, sentence structure, and vocabulary in \
context. Three tested writing skills. English is nine marks; an hour spent on tenses, prepositions \
and confusable word pairs is enough, and a second hour is wasted.

These counts are a snapshot taken on 12 September 2026 from our verified question bank. Our \
[Biology chapter-wise weightage analysis](/blog/mdcat-biology-chapter-wise-weightage) runs the same \
method across all 16 papers if you want the longer view.

## The 8-day plan

One rule underneath all of it: **no new topic after Wednesday.** Anything you start learning in the \
last four days competes for memory with things you already know, and it usually wins. That trade is \
a bad one.

**Sunday 13 September — Biology, high-yield first.** Biological Molecules, Cell Structure, \
Coordination and Control. Read your own notes, not a textbook. Then 60 mixed Biology MCQs from a \
past paper and mark every wrong answer.

**Monday 14 September — Biology, second half plus Chemistry organic.** Support and Movement, \
Reproduction, Inheritance. Then Hydrocarbons and Fundamental Principles of Organic Chemistry, which \
are 33 marks between them across recent papers.

**Tuesday 15 September — Chemistry, physical and inorganic.** Chemical Bonding, Atomic Structure, \
Equilibrium, Thermochemistry, Gases. Work through the numericals with a pen. Reading a solved \
example is not the same skill as producing it under time.

**Wednesday 16 September — Physics.** Force and Motion, Work and Energy, and the whole electricity \
and magnetism block, which is 52 marks across the last four papers. Rebuild your formula sheet from \
memory, then check it. The gaps you find are your revision list, and this is the last day for new \
material.

**Thursday 17 September — one full mock, timed.** Three hours, no phone, no breaks, morning if you \
can. Score it the same day and sort your mistakes into three piles: did not know it, knew it but \
misread it, knew it but ran out of time. Those three piles need three different fixes, and only the \
first one is about syllabus.

**Friday 18 September — fix the mock.** Work only on what the mock exposed. Redo those exact \
questions, then a short set on the same topics. Add one English hour: grammar and vocabulary drills. \
Stop by evening.

**Saturday 19 September — light and administrative.** A one-hour skim of your formula sheet and \
Biology diagrams, and nothing else academic. Assemble your documents, check the exam centre address \
and the route, and sleep at your normal time. Do not sit a mock today. A bad score the night before \
does nothing except damage the exam you are about to sit.

**Sunday 20 September — exam day.** Covered below.

If you are behind on this plan, do not try to compress it. Drop the lowest-yield half of each day \
and keep the mock on Thursday. The mock is the part that most reliably adds marks.

## What to stop doing this week

**Stop starting new chapters.** Eight days is retrieval time, not intake time.

**Stop passive reading.** Recall beats rereading at this stage by a wide margin. Close the book and \
say the pathway out loud, then check it.

**Stop sitting mocks you do not review.** An unreviewed mock costs you three hours and teaches you \
nothing. One mock properly reviewed is worth four taken and forgotten.

**Stop comparing scores.** Somebody in your group is lying about theirs, and it will not be on the \
paper with you.

**Stop the all-nighters now, not on Saturday.** Sleep is where the last week's revision is \
consolidated. A 2 a.m. finish on Thursday costs you marks on Sunday.

## Exam day

**Bring what your roll number slip says to bring.** PMDC and the conducting university publish the \
binding list on the slip itself, and it changes between sittings, so read yours rather than a list \
on the internet. In practice that has meant a printed roll number slip and your original CNIC or \
B-Form. Phones, smartwatches and calculators do not come in.

**Reach the centre early.** Traffic on exam morning is its own exam. The reporting time on your slip \
is a deadline, not a suggestion, and centres close their gates.

**Fill the OMR sheet as you go, not at the end.** Every year candidates run out of time with a \
completed question paper and a half-filled answer sheet. That is not a knowledge problem, and it is \
entirely avoidable.

**Do not stall on a hard question.** At 180 questions in 180 minutes you have a minute each. Mark \
it, move, come back. A minute spent on question 12 is a mark lost on question 170.

**Answer all 180.** There is no negative marking. Eliminate what you can, then commit to a bubble. \
An empty answer is the only guaranteed zero on the paper.

**When a question looks unfamiliar, read it again before panicking.** Most MDCAT questions are the \
familiar concept in unfamiliar clothes.

## Practise with real papers, not predictions

Every September brings "guess papers" and leaked-pattern claims. Ignore them. The one thing that \
reliably predicts MDCAT is MDCAT.

On ParhaiKrlo you can sit **16 verified past papers — 3,363 questions**, every answer key checked \
against the official key question by question, and **20 full-length mocks** timed exactly like the \
real paper. Wrong answers come with an explanation, so a review session is actually a study session.

Start with [MDCAT past papers](/past-papers) — our [year-wise guide](/blog/mdcat-past-papers-guide) says which years to sit first — then take a [full mock](/mocks) on Thursday, and use the \
[syllabus tree](/syllabus) to drill any topic the mock exposes. Good luck on the 20th.
"""

FAQS = [
    {
        'question': 'When is MDCAT 2026?',
        'answer': (
            'MDCAT 2026 is scheduled for Sunday, 20 September 2026, rescheduled from the original '
            '16 August date. It is a paper-based test of 180 MCQs over 3 hours.'
        ),
    },
    {
        'question': 'Can I still improve my MDCAT score in the last week?',
        'answer': (
            'Yes, but by revising and practising, not by learning new chapters. Most last-week gains '
            'come from timed practice, reviewing mistakes, and fixing OMR and time-management habits '
            'rather than from new content.'
        ),
    },
    {
        'question': 'Which MDCAT topics are highest-yield in the final week?',
        'answer': (
            'Across the 2022-2025 papers, ten Biology units carried 91% of Biology questions, led by '
            'Biological Molecules, Cell Structure and Function, Coordination and Control, and Support '
            'and Movement. In Physics, Force and Motion, Work and Energy, and the electricity and '
            'magnetism block dominate. Chemistry is the flattest subject, with Hydrocarbons and '
            'Chemical Bonding on top.'
        ),
    },
    {
        'question': 'Is there negative marking in MDCAT 2026?',
        'answer': (
            'No. MDCAT has no negative marking, so leaving a question blank can only lose you marks. '
            'Eliminate what you can and answer all 180 questions.'
        ),
    },
    {
        'question': 'How many marks do I need to pass MDCAT 2026?',
        'answer': (
            'The passing threshold is 55% (99 out of 180) for medical admission and 50% (90 out of '
            '180) for dental. Passing is only the eligibility bar — actual admission depends on merit '
            'in your province and institution.'
        ),
    },
    {
        'question': 'Should I take a mock test the day before MDCAT?',
        'answer': (
            'No. Sit your last full mock about three days out, on Thursday 17 September, so you have '
            'time to act on what it exposes. The day before should be a light skim, document checks, '
            'and normal sleep.'
        ),
    },
    {
        'question': 'How many past papers should I solve before MDCAT 2026?',
        'answer': (
            'Quality beats quantity in the last week. One fully reviewed past paper or mock, with '
            'every mistake classified and fixed, is worth more than three sat and forgotten. Aim for '
            'one timed full-length paper plus targeted sets on your weak topics.'
        ),
    },
    {
        'question': 'What should I bring to the MDCAT exam centre?',
        'answer': (
            'Follow the list printed on your own roll number slip, since the conducting university '
            'sets it per sitting. In practice that has meant a printed roll number slip and your '
            'original CNIC or B-Form. Phones, smartwatches and calculators are not allowed inside.'
        ),
    },
    {
        'question': 'Are MDCAT guess papers worth using?',
        'answer': (
            'No. Guess papers and leaked-pattern claims circulate every September and have no '
            'official basis. Past papers are the only material that reflects how PMDC actually asks '
            'questions.'
        ),
    },
    {
        'question': 'What is the MDCAT 2026 paper pattern?',
        'answer': (
            '180 MCQs in 180 minutes: Biology 81, Chemistry 45, Physics 36, English 9 and Logical '
            'Reasoning 9. The 2025 paper already followed this exact split.'
        ),
    },
]


class Command(BaseCommand):
    help = 'Seeds/updates the MDCAT 2026 final-week revision plan blog post.'

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
