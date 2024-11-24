from django.shortcuts import render
from .forms import ExampleForm
from .models import Book


def search_books(request):
    query = request.GET.get("query", "")
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books})


from .forms import BookSearchForm


def search_books(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data["query"]
        books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"form": form, "books": books})
