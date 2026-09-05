from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'is_published', 'is_pinned', 'published_at', 'updated_at')
    list_filter = ('post_type', 'is_published', 'is_pinned')
    search_fields = ('title', 'slug', 'excerpt', 'body', 'meta_title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published', 'is_pinned')
    date_hierarchy = 'published_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'post_type', 'excerpt', 'body', 'cover_image_url', 'author_name'),
        }),
        ('SEO (optional — falls back to title/excerpt above if left blank)', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',),
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_pinned', 'published_at'),
        }),
    )
