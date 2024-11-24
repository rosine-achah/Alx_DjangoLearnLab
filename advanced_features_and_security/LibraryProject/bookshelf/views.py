from django.shortcuts import render

from .models import Book


def search_books(request):
    query = request.GET.get("query", "")
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books})
