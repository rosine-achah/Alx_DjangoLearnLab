from django.urls import path
from .views import NotificationListView

urlpatterns = [
    path("", NotificationListView.as_view(), name="notifications"),
]

from django.urls import path
from .views import NotificationViewSet

notification_list = NotificationViewSet.as_view({"get": "list"})

urlpatterns = [
    path("notifications/", notification_list, name="notification-list"),
]
