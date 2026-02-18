from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    # Task 0 & 2: Authentication
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # Task 2: Profile Management
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Task 2: Follow Management
    # Requirement: follow/int:user_id/ and unfollow/int:user_id/
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]