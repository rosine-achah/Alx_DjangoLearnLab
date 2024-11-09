from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/", LibraryDetailView, name="LibraryDetailView"),
]
