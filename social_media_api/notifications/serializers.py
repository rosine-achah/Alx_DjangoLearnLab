from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Notification
        fields = [
            "id",
            "sender",
            "receiver",
            "notification_type",
            "post",
            "created_at",
            "is_read",
        ]
