from relationship_app.models import *

def get_book(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def list_all_books(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def retrieve(library_name):
    library = Library.objects.get(name=library_name)
    return library.libarien

    
