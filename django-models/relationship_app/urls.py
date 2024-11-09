from django.urls import path
from . import views
from .views import list_books, LibraryDetails

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/", LibraryDetails, name="LibraryDetails"),
]
