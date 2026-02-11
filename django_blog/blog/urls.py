from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView, CommentCreateView,
    CommentUpdateView, CommentDeleteView, PostByTagListView,
    SearchResultsView, register, profile # Import your auth views
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Auth URLs (Requirement for Task 1)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    # Post URLs (Requirement for Task 2)
    path('', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs (Requirement for Task 3)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Search and Tagging (Requirement for Task 4)
    path('search/', SearchResultsView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
]