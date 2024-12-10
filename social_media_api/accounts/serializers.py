from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "bio", "profile_picture"]


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["key"]
