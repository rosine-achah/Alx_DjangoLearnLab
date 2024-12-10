from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProfileView
from .views import UserRegistrationView, CustomAuthToken

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("api/token/refresh/", TokenObtainPairView.as_view(), name="token_refresh"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("login/", CustomAuthToken.as_view(), name="user-login"),
]


# Authorization: Bearer your_access_token
