from django.urls import path 
from . import views 
from .views import book_list
from .views import LibraryDetails

urlpatterns = [
     path('books/', list_books, name = "list_books")
     path('library/', LibraryDetails, name = "LibraryDetails" )
]
