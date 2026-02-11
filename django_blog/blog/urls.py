from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, CommentCreateView,
    CommentUpdateView, CommentDeleteView, PostByTagListView,
    SearchResultsView
)

urlpatterns = [
    # Post URLs (Task 2)
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs (Task 3)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Search and Tagging URLs (Task 4)
    path('search/', SearchResultsView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
]