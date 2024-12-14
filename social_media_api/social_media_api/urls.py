"""
URL configuration for social_media_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("accounts/", include("accounts.urls")),
    path("api/accounts/", include("accounts.urls")),
    path("api/accounts/", include("accounts.urls")),
    path("api/posts", include("posts.urls")),
    path("notifications/", include("notifications.urls")),
]

from django.urls import path
from .views import PostViewSet

post_list = PostViewSet.as_view({"get": "list", "post": "create"})
post_detail = PostViewSet.as_view(
    {"get": "retrieve", "put": "update", "delete": "destroy"}
)
post_like = PostViewSet.as_view({"post": "like_post"})
post_unlike = PostViewSet.as_view({"delete": "unlike_post"})

urlpatterns = [
    path("posts/", post_list, name="post-list"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
    path("posts/<int:pk>/like/", post_like, name="post-like"),
    path("posts/<int:pk>/unlike/", post_unlike, name="post-unlike"),
]
