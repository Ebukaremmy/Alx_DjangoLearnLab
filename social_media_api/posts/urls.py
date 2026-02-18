from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView

# Initialize the router for ViewSets
router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    # The 'feed/' endpoint must come before the router urls
    path('feed/', FeedView.as_view(), name='user-feed'),
    
    # This includes all the routes for posts and comments (GET, POST, PUT, DELETE)
    path('', include(router.urls)),
]