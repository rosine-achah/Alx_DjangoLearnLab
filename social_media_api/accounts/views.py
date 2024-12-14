from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import UserSerializer, TokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.views import View
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .models import Post
from .serializers import PostSerializer
from django.views import View
from django.http import JsonResponse
from rest_framework.decorators import action

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProfileView(RetrieveUpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user


User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        user = super().post(request, *args, **kwargs)
        toke, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class RegisterView(View):
    def get(self, request):
        return render(request, "registration.html")

    def post(self, request):
        pass


class ProfileView(View):
    def get(self, request):
        # Placeholder for profile data
        profile_data = {
            "username": request.user.username,
            "email": request.user.email,
            # Add more user info as needed
        }
        return JsonResponse(profile_data)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({"message": "You are now following this user. "})


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "You have unfollowed this user. "})


class FeedView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            author__in=self.request.user.following.all()
        ).order_by("-created_at")


class FollowViewSet(viewsets.ViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]  # Ensure only authenticated users can access these actions

    @action(detail=False, methods=["post"])
    def follow_user(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            request.user.following.add(
                user_to_follow
            )  # Assuming 'following' is the ManyToMany field
            return Response(
                {"message": f"You are now following {user_to_follow.username}."}
            )
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

    @action(detail=False, methods=["post"])
    def unfollow_user(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            request.user.following.remove(
                user_to_unfollow
            )  # Assuming 'following' is the ManyToMany field
            return Response(
                {"message": f"You have unfollowed {user_to_unfollow.username}."}
            )
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)
