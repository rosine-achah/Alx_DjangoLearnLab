from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Follow
from django.db.models import Q


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        Notification.objects.create(
            sender=self.request.user,
            receiver=comment.post.author,
            notification_type="comment",
            post=comment.post,
        )


class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user_to_follow = User.objects.get(username=username)
        if Follow.objects.filter(
            follower=request.user, following=user_to_follow
        ).exists():
            return Response(
                {"detail": "You are already following this user."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        Follow.objects.create(follower=request.user, following=user_to_follow)

        # Create nottification
        Notification.objects.create(
            sender=request.user, reciever=user_to_follow, notification_type="follow"
        )

        return Response(
            {"detail": f"You are now following {user_to_follow.username}."},
            status=status.HTTP_201_CREATED,
        )


class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        user_to_unfollow = User.objects.get(username=username)
        follow_relationship = Follow.objects.filter(
            follower=request.user, following=user_to_unfollow
        )
        if not follow_relationship.exists():
            return Response(
                {"detail": "You are not following this user."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        follow_relationship.delete()
        return Response(
            {"detail": f"You have unfollowed {user_to_unfollow.username}."},
            status=status.HTTP_204_NO_CONTENT,
        )


class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followed_users = Follow.objects.filter(follower=request.user).values_list(
            "following", flat=True
        )
        posts = Post.objects.filter(author_in=followed_users).order_by("created_at")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response(
                {"detail": "You already liked this post"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Like.objects.create(user, request.user, post=post)

        # Create notification

        Notification.objects.create(
            sender=request.user,
            receiver=post.author,
            notification_type="like",
            post=post,
        )

        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)
