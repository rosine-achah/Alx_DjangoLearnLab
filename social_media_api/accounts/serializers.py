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


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "bio", "profile_picture"]
        extra_kwargs = {"password": {"write_only": True}}

    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(**validated_data)
    #     return user
    def create(self, validated_data):
        # Remove the password from the data to hash it properly
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()

        Token.objects.create(user=user)
        return user
