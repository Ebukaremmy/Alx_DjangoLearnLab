from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Fixed the typo here: admin.site.urls
    path('admin/', admin.site.urls),
    
    # This connects your 'api' app routes
    path('api/', include('api.urls')),
    
    # Task 3: This allows users to get an auth token
    path('api-token-auth/', obtain_auth_token),
]