from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FollowUserView, UnfollowUserView, FeedView

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += [
    path("follow/<str:username>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<str:username>/", UnfollowUserView.as_view(), name="unfollow-user"),
    path("feed/", FeedView.as_view(), name="user-feed"),
    path("feed/", FeedView.as_view(), name="feed"),
]
