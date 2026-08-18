from django.urls import path
from .views import PinnedAnnouncementView, PostDetailView, PostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('announcement/', PinnedAnnouncementView.as_view(), name='pinned-announcement'),
]
