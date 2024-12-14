from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import CustomUser

User = get_user_model()


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ["id", "username", "email", "bio", "profile_picture"]


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["key"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        # write_only=True, required=True, style={"input_type": "password"}
    )

    class Meta:
        model = User  # CustomUser
        fields = ["username", "password", "email", "bio", "profile_picture"]
        extra_kwargs = {"password": {"write_only": True}}

    # def create(self, validated_data):
    #     user = CustomUser.objects.create_user(**validated_data)
    #     return user
    def create(self, validated_data):
        password = validated_data.pop("password")

        # user = CustomUser(**validated_data)
        # user.set_password(password)  # Hash the password
        # user.save()
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            bio=validated_data.get("bio"),
            profile_picture=validated_data.get("profile_picture"),
            password=password,
        )

        Token.objects.create(user=user)
        return user
