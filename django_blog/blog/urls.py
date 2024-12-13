from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register
from .views import profile
from . import views
from .views import CommentUpdateView  # Import the new view
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    # path("post/<int:pk>/", views.PostDetailView, name="post_detail"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("comments/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
    path("post/<int:post_id>/comments/new/", views.add_comment, name="add_comment"),
    path(
        "post/<int:post_id>/comments/<int:comment_id>/edit/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "post/<int:post_id>/comments/<int:comment_id>/delete/",
        views.delete_comment,
        name="delete_comment",
    ),
    path(
        "comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit_comment"
    ),  # Add this line
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    # path("login/", views.user_login, name="login"),
    # path("logout/", views.user_logout, name="logout"),
    # path("posts/", PostListView.as_view(), name="post_list"),
    # path("posts/<int:pk>/", PostListView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
