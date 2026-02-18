from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView

# Initialize the router for ViewSets (Task 2)
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # Requirement: Route for the feed endpoint /feed/
    path('feed/', FeedView.as_view(), name='post-feed'),
    
    # Requirement: Routes for liking and unliking posts
    # Matches: /posts/<int:pk>/like/ and /posts/<int:pk>/unlike/
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    
    # Include the router urls for posts/ and comments/
    path('', include(router.urls)),
]