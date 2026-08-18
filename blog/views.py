from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostDetailSerializer, PostListSerializer


class PostListView(generics.ListAPIView):
    """GET /api/blog/posts/?type=blog|announcement — published posts, newest/pinned first."""
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    pagination_class = None  # small content volume, no need to paginate yet

    def get_queryset(self):
        qs = Post.objects.filter(is_published=True)

        post_type = self.request.query_params.get('type')
        if post_type in dict(Post.TYPE_CHOICES):
            qs = qs.filter(post_type=post_type)

        return qs


class PostDetailView(generics.RetrieveAPIView):
    """GET /api/blog/posts/<slug>/ — full post body."""
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PinnedAnnouncementView(APIView):
    """
    GET /api/blog/announcement/

    The single most recent pinned + published announcement, if any.
    Powers the app-wide announcement banner.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        post = (
            Post.objects.filter(
                is_published=True,
                is_pinned=True,
                post_type='announcement',
            )
            .order_by('-published_at', '-created_at')
            .first()
        )

        if not post:
            return Response({'available': False})

        return Response({
            'available': True,
            'post': PostDetailSerializer(post).data,
        })
