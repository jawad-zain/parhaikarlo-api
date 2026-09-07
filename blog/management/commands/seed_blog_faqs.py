from django.core.management.base import BaseCommand

from blog.models import Post

# Every answer here is pulled directly from the matching post's own body
# copy — no numbers, dates, or claims invented. Keep these two in sync with
# the visible body text if either post's copy is ever edited; the frontend
# renders this exact text both on-page and in FAQPage JSON-LD, so a mismatch
# here becomes a Google Search Console mismatch there.
FAQS_BY_SLUG = {
    'mdcat-past-papers-guide': [
        {
            'question': 'Are MDCAT past papers enough to prepare?',
            'answer': (
                "Past papers are the single highest-ROI resource for MDCAT prep — more useful than "
                "textbooks, YouTube lectures, or expensive academies. But they work best paired with "
                "the syllabus, not alone: textbook practice makes you know the syllabus, while past "
                "papers make you ready for the exam. Use both together rather than relying on past "
                "papers by themselves."
            ),
        },
        {
            'question': 'How many MDCAT past papers should I solve before the exam?',
            'answer': (
                "At least 10+ past papers — a student who has seriously worked through that many walks "
                "into the exam hall with a real information advantage. Weight your practice toward the "
                "PMDC-era papers (2022 onward), since that's the current format you'll actually sit, and "
                "save your three most recent papers (2023, 2024, 2025) for timed practice closer to exam day."
            ),
        },
        {
            'question': 'Where can I find MDCAT 2020 and 2021 past papers?',
            'answer': (
                "Papers from the 2020–2021 transition window are hard to source in reliable form and are "
                "being added carefully after verification, so they're not listed yet. Don't panic if you "
                "don't see them — the old UHS-era papers (2008–2019) and the current PMDC-era papers "
                "(2022–2025) still give you the depth and format practice you need."
            ),
        },
        {
            'question': 'Do MDCAT questions repeat every year?',
            'answer': (
                "Not the exact questions, but the patterns do. UHS and PMDC recycle question patterns, "
                "favourite topics, and even exact concepts year after year — around 60–70% of questions "
                "each year test the same core topics, like genetics ratios in biology, stoichiometry in "
                "chemistry, and kinematics and electromagnetism in physics. That's why past papers show you "
                "exactly which sub-topics UHS actually asks about, at what difficulty and wording style."
            ),
        },
        {
            'question': 'Should I solve past papers timed or untimed?',
            'answer': (
                "Both, in that order. In the middle of your prep (weeks 8–12), sit full papers untimed, "
                "open-book allowed for concepts you get stuck on, so the goal is understanding every "
                "question rather than racing. In your final 4–6 weeks, switch to strictly timed papers "
                "under 3.5 hours in mock conditions, using your most recent papers as the most accurate simulators."
            ),
        },
    ],
    'mdcat-2026-syllabus': [
        {
            'question': 'When is MDCAT 2026?',
            'answer': (
                "MDCAT 2026 is on Sunday, 20 September 2026. It was rescheduled from the originally "
                "planned date of 16 August."
            ),
        },
        {
            'question': 'What is the passing marks for MDCAT 2026?',
            'answer': (
                "Passing marks are 55% (99 out of 180) for medical and 50% (90 out of 180) for dental. "
                "The paper is 180 MCQs total, each worth 1 mark, with no negative marking."
            ),
        },
        {
            'question': 'Is there negative marking in MDCAT?',
            'answer': (
                "No — MDCAT has no negative marking, so you should attempt every question. Even for "
                "questions you don't know, take an educated guess, since you have nothing to lose by "
                "leaving nothing blank."
            ),
        },
        {
            'question': 'What is the MDCAT 2026 subject-wise weightage?',
            'answer': (
                "Out of 180 total MCQs: Biology is 81 MCQs (45%), Chemistry is 45 MCQs (25%), Physics is "
                "36 MCQs (20%), English is 9 MCQs (5%), and Logical Reasoning is 9 MCQs (5%). Biology and "
                "Chemistry together make up 70% of the paper, so getting those two subjects right secures "
                "most of your score."
            ),
        },
        {
            'question': 'Has the MDCAT syllabus changed for 2026?',
            'answer': (
                "No. This syllabus is verified against the official PMDC MDCAT 2025 Curriculum PDF (dated "
                "26 May 2025), and PMDC has confirmed it applies unchanged to MDCAT 2026."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = (
        "Populate the `faqs` field on specific blog posts by slug, from the FAQS_BY_SLUG "
        "content map in this file. Idempotent — safe to re-run after editing the map."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--slug', action='append', dest='slugs', default=None,
            help='Limit to one or more slugs (repeatable). Defaults to every slug in the map.',
        )

    def handle(self, *args, **options):
        slugs = options['slugs'] or list(FAQS_BY_SLUG.keys())

        for slug in slugs:
            faqs = FAQS_BY_SLUG.get(slug)
            if faqs is None:
                self.stderr.write(self.style.WARNING(f'No FAQ content mapped for slug "{slug}" — skipped.'))
                continue

            try:
                post = Post.objects.get(slug=slug)
            except Post.DoesNotExist:
                self.stderr.write(self.style.ERROR(f'No Post with slug "{slug}" found — skipped.'))
                continue

            post.faqs = faqs
            post.save(update_fields=['faqs'])
            self.stdout.write(self.style.SUCCESS(f'Set {len(faqs)} FAQ(s) on "{slug}".'))
