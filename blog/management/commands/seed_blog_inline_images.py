from django.core.management.base import BaseCommand

from blog.models import Post

# `insert_after_heading` must match the post's own H2 text exactly (the
# frontend compares loosely — trimmed, case-insensitive — but keep it exact
# here so a straight text search in the body finds it). If either post's
# heading text changes, update the matching entry here too.
INLINE_IMAGES_BY_SLUG = {
    'mdcat-past-papers-guide': [
        {
            'slug': 'mdcat-eras-timeline',
            'src': '/blog/mdcat-eras-timeline.svg',
            'alt': (
                "MDCAT paper format across three eras: Old UHS (2008–2019, 200–220 MCQs, "
                "no Logical Reasoning), Transition (2020–2021), PMDC (2022–2025, 200 MCQs "
                "with Logical Reasoning)"
            ),
            'caption': "How the MDCAT paper structure has shifted across three eras.",
            'width': 720,
            'height': 380,
            'insert_after_heading': "Three eras of MDCAT — what changed and why it matters",
        },
    ],
    'mdcat-2026-syllabus': [
        {
            'slug': 'mdcat-2026-weightage-chart',
            'src': '/blog/mdcat-2026-weightage-chart.svg',
            'alt': (
                "MDCAT 2026 subject-wise weightage: Biology 45%, Chemistry 25%, Physics 20%, "
                "English 5%, Logical Reasoning 5%"
            ),
            'caption': "MDCAT 2026 marks distribution across the five subjects.",
            'width': 720,
            'height': 400,
            'insert_after_heading': "Subject-wise weightage",
        },
    ],
}


class Command(BaseCommand):
    help = (
        "Populate the `inline_images` field on specific blog posts by slug, from the "
        "INLINE_IMAGES_BY_SLUG content map in this file. Idempotent — safe to re-run "
        "after editing the map. Mirrors seed_blog_faqs."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            '--slug', action='append', dest='slugs', default=None,
            help='Limit to one or more slugs (repeatable). Defaults to every slug in the map.',
        )

    def handle(self, *args, **options):
        slugs = options['slugs'] or list(INLINE_IMAGES_BY_SLUG.keys())

        for slug in slugs:
            images = INLINE_IMAGES_BY_SLUG.get(slug)
            if images is None:
                self.stderr.write(self.style.WARNING(f'No inline-image content mapped for slug "{slug}" — skipped.'))
                continue

            try:
                post = Post.objects.get(slug=slug)
            except Post.DoesNotExist:
                self.stderr.write(self.style.ERROR(f'No Post with slug "{slug}" found — skipped.'))
                continue

            post.inline_images = images
            post.save(update_fields=['inline_images'])
            self.stdout.write(self.style.SUCCESS(f'Set {len(images)} inline image(s) on "{slug}".'))
