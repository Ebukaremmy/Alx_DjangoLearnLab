from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # Requirement: Must contain 'generics.get_object_or_404(Post, pk=pk)'
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Requirement: Must contain 'Like.objects.get_or_create(user=request.user, post=post)'
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Requirement: Must contain 'Notification.objects.create'
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
        return Response(status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)