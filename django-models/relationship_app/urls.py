from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView, LoginView

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/", LibraryDetailView, name="LibraryDetailView"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/".LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("admin/", views.admin_view, name="admin_view"),
    path("librarian/", views.librarian_view, name="librarian_view"),
    path("member/", views.member_view, name="member_view"),
]
