from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetails(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

    context_object_name = Library
