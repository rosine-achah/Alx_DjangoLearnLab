from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register
from .views import profile
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile "),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostListView.as_view(), name="post_detail"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
