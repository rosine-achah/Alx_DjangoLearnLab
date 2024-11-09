Command:
Book.objects.get()
get_book = Book.objects.get(title = "1984")
print(get_book.title, get_book.author, get_book.publication_year)

Expected_output:
1984, George Orwell, 1949
