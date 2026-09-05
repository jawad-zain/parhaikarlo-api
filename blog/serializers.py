from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    """List view — no body, keeps the /posts/ payload light."""

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'post_type', 'excerpt',
            'meta_title', 'meta_description',
            'cover_image_url', 'author_name', 'is_pinned', 'published_at',
            'updated_at',
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'post_type', 'excerpt', 'body',
            'meta_title', 'meta_description',
            'cover_image_url', 'author_name', 'is_pinned', 'published_at',
            'updated_at',
        ]
