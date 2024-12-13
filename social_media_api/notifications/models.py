from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from django.conf import settings


# Create your models here.
class Notification(models.Model):
    TYPE_CHOICES = [
        ("follow", "Follow"),
        ("comment", "Comment"),
        ("like", "Like"),
    ]

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sent_notifications",
        on_delete=models.CASCADE,
    )
    reciever = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recieved_notification",
        on_delete=models.CASCADE,
    )
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.sender.username} {self.notification_type} {self.reciever.username}"
        )
