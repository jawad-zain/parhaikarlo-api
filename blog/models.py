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

    # Plain external URL rather than an upload field — keeps this app free
    # of media-serving concerns; paste an image host link if you want one.
    cover_image_url = models.URLField(blank=True)

    author_name = models.CharField(max_length=120, blank=True)

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
