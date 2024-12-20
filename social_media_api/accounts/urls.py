from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProfileView
from .views import UserRegistrationView, CustomAuthToken
from .views import UserRegistrationView
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("api/token/refresh/", TokenObtainPairView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", CustomAuthToken.as_view(), name="user-login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow_user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow_user"),
]

urlpatterns += [
    path("register/", UserRegistrationView.as_view(), name="register"),
]
# Authorization: Bearer your_access_token
