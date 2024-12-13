# from django.urls import path
# from .views import CustomLoginView, CustomLogoutView, register
# from .views import profile
# from . import views
# from .views import CommentUpdateView  # Import the new view
# from .views import (
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
# )

# from django.urls import path
# from .views import (
#     CustomLoginView,
#     CustomLogoutView,
#     register,
#     profile,
#     PostListView,
#     PostDetailView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     add_comment,
#     edit_comment,
#     delete_comment,
#     CommentUpdateView,
# )


# path("", views.PostListView.as_view(), name="post_list"),
# path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
# path("login/", CustomLoginView.as_view(), name="login"),
# path("logout/", CustomLogoutView.as_view(), name="logout"),
# path("comments/<int:comment_id>/edit/", views.edit_comment, name="edit_comment"),
# path("post/<int:post_id>/comments/new/", views.add_comment, name="add_comment"),
# path(
#     "post/<int:post_id>/comments/<int:comment_id>/edit/",
#     views.edit_comment,
#     name="edit_comment",
# ),
# path(
#     "post/<int:post_id>/comments/<int:comment_id>/delete/",
#     views.delete_comment,
#     name="delete_comment",
# ),
# path(
#     "comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit_comment"
# ),  # Add this line
# path("register/", views.register, name="register"),
# path("profile/", views.profile, name="profile"),
# path("post/new/", PostCreateView.as_view(), name="post_create"),
# path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
# path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),


from django.urls import path
from . import views
from .views import search_posts
from .views import (
    CustomLoginView,
    CustomLogoutView,
    register,
    profile,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    edit_comment,
    delete_comment,
    CommentUpdateView,
)

urlpatterns = [
    # Post URLs
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    # Comment URLs
    path(
        "post/<int:pk>/comments/new/", add_comment, name="add_comment"
    ),  # URL to add a new comment
    path(
        "comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit_comment"
    ),  # URL to edit a comment
    path(
        "comment/<int:pk>/delete/", delete_comment, name="delete_comment"
    ),  # URL to delete a comment
    path(
        "comment/<int:pk>/update/", CommentUpdateView.as_view(), name="update_comment"
    ),  # URL to update a comment
    # Authentication URLs
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("search/", search_posts, name="search_posts"),  # URL for search functionality
    path(
        "tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"
    ),  # URL to filter posts by tag
]
