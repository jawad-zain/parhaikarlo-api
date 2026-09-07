from django.db import models
from django.utils import timezone


class Post(models.Model):
    """A blog article or a site-wide announcement.

    One model for both — they share every field, and "Blog/Announcements"
    was always one deliverable, not two. post_type is what a reader-facing
    page filters on; is_pinned lets an announcement float to the top (and
    surface in the app-wide announcement banner).
    """

    TYPE_CHOICES = [
        ('blog', 'Blog'),
        ('announcement', 'Announcement'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    post_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='blog')

    excerpt = models.CharField(
        max_length=300, blank=True,
        help_text='Short teaser shown on the list page. Falls back to a trimmed body if left blank.',
    )
    body = models.TextField()  # Markdown allowed — rendered as-is on the frontend for now.

    # SEO overrides — optional. The frontend's <title>/meta-description and
    # Open Graph/Twitter tags fall back to title/excerpt when these are
    # blank, so most posts never need to touch them. They exist for cases
    # where the on-page title reads well but is too long for a SERP title
    # (~60 chars) or the excerpt runs past a meta description's ~155-160
    # char display limit before Google truncates it.
    meta_title = models.CharField(
        max_length=70, blank=True,
        help_text='Overrides the <title>/og:title for search & social. Falls back to title. Keep to ~60 chars.',
    )
    meta_description = models.CharField(
        max_length=160, blank=True,
        help_text='Overrides the meta/og description. Falls back to excerpt. Keep to ~155 chars.',
    )

    # Plain external URL rather than an upload field — keeps this app free
    # of media-serving concerns; paste an image host link if you want one.
    cover_image_url = models.URLField(blank=True)

    author_name = models.CharField(max_length=120, blank=True)

    # Optional FAQ block rendered near the bottom of the post and emitted as
    # FAQPage JSON-LD. List of {"question": str, "answer": str}. Empty list
    # (the default) means "no FAQ section" — the frontend and the JSON-LD
    # builder both skip it entirely rather than rendering an empty heading.
    faqs = models.JSONField(
        default=list, blank=True,
        help_text='Optional FAQ list: [{"question": "...", "answer": "..."}, ...]. '
                   'Leave empty to skip the FAQ section on this post.',
    )

    # Optional in-body images. List of:
    #   {"slug": str, "src": str, "alt": str, "caption": str (optional),
    #    "width": int, "height": int, "insert_after_heading": str | None}
    # `slug` is a stable id for this image entry — future edits reorder or
    # restyle by slug, never by array position. `insert_after_heading` is
    # the exact text of the H2 the image renders after (case/whitespace
    # compared loosely on the frontend); null means "insert at the top" of
    # the body. Empty list (the default) means no inline images.
    inline_images = models.JSONField(
        default=list, blank=True,
        help_text='Optional in-body images: [{"slug": "...", "src": "/blog/foo.svg", '
                   '"alt": "...", "caption": "...", "width": 720, "height": 400, '
                   '"insert_after_heading": "Exact H2 text" or null}, ...].',
    )

    is_published = models.BooleanField(default=False)
    is_pinned = models.BooleanField(
        default=False,
        help_text='Pinned + published + announcement shows in the app-wide banner.',
    )
    published_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-published_at', '-created_at']

    def __str__(self):
        return f'[{self.get_post_type_display()}] {self.title}'

    def save(self, *args, **kwargs):
        # Stamp published_at the first time a post goes live, so ordering
        # and "published X ago" copy have something real to work with.
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
