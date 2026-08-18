from django.core.management.base import BaseCommand
from founder.models import BuildTask


TASKS = [
    # Week 1 — Setup
    (1, 'Django + PostgreSQL scaffold', True),
    (1, 'Landing page (Next.js on Vercel)', True),
    (1, 'Content schema (Exam/Subject/Topic/Subtopic/Question/ConceptNote)', True),
    (1, 'Domain + brand chosen (parhaikarlo.com)', True),

    # Week 2-3 — Content ingest
    (2, 'PDF extraction pipeline (parser + adapter routes)', True),
    (2, 'Topic tagging via Groq (batch, closed vocab)', True),
    (2, 'Ingest 10 past papers (2014-2025)', True),
    (3, 'Friend-verified answer key applied to full DB', True),
    (3, 'Duplicate-options detector + cleanup', False),

    # Week 4 — User + Attempt + Mock + Progress
    (4, 'JazzCash merchant application', False),
    (4, 'User + StudentProfile models', True),
    (4, 'JWT auth (email/password + Google Sign-In)', True),
    (4, 'Attempt + AttemptQuestion models', True),
    (4, 'Core APIs (questions, attempts, answer, submit, review)', True),
    (4, 'Scoring engine (per-subject/topic accuracy)', True),
    (4, 'MockTest model + full mock endpoint', True),
    (4, 'UserProgress model + recompute on submit', True),
    (4, 'Founder admin dashboard', False),
    (4, 'Break mechanic (AttemptBreak + start/end endpoints)', False),
    (4, 'Mock integrity (AttemptViolation + violation flow)', False),

    # Week 5 — AI layer
    (5, 'Explain endpoint (3-layer JSON, DB cache)', False),
    (5, 'Groq integration with MODEL_PROVIDER switch', False),
    (5, 'Rate limiting (5/day free, 50/day paid)', False),
    (5, 'Prompt iteration on 5+ real Qs per subject', False),
    (5, 'Admin "Ask my platform" Claude chatbot', False),

    # Week 6-7 — Practice engine + weak topics
    (6, 'Weak-topic weighting in question selector', False),
    (6, 'Already-seen Q exclusion', False),
    (7, 'Weak Topics Drill (unlocks after 5 sessions)', False),
    (7, 'Bookmarks (save Q for later)', False),
    (7, 'Quick 20 (subject-agnostic quick practice)', False),

    # Week 8 — Frontend integration
    (8, 'Split-Screen Reading Room MCQ card (desktop)', False),
    (8, 'Mobile MCQ card (torn-page divider)', False),
    (8, 'Practice / Mock / Past Paper / Syllabus / Dashboard tabs', False),
    (8, 'Explain button wired to backend endpoint', False),
    (8, 'Blog/Announcements CMS + first 3 posts', False),

    # Week 9 — Verifier + payment
    (9, 'Content verifier tutor onboarded (or self-verify decision)', False),
    (9, 'JazzCash payment flow', False),
    (9, 'Subscription model + paywall gating', False),

    # Week 10 — Polish + beta
    (10, 'Weekly national live mock (Sunday 7pm)', False),
    (10, 'Parent weekly report email (PDF via ReportLab)', False),
    (10, 'Referral system (30-day bonus per referral)', False),
    (10, '10 beta users onboarded', False),

    # Week 11 — Growth features
    (11, 'City-wise leaderboard', False),
    (11, 'Streak protection (1 skip day/week)', False),
    (11, 'Percentile predictor calibration', False),

    # Week 12 — Launch
    (12, 'Rs 15k ad spend live (Instagram + Facebook)', False),
    (12, 'First paying user', False),
    (12, 'Public launch (WhatsApp groups, Insta reels, FB group posts)', False),
]


class Command(BaseCommand):
    help = 'Seed the BuildTask table with the 12-week plan.'

    def handle(self, *args, **options):
        created = 0
        for order, (week, title, is_done) in enumerate(TASKS):
            _, was_created = BuildTask.objects.get_or_create(
                week=week,
                title=title,
                defaults={'is_done': is_done, 'order': order},
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(
            f'Seeded {created} new tasks ({len(TASKS) - created} already existed).'
        ))