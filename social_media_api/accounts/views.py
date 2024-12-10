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
