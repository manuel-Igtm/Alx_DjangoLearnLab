from relationship_app.models import Author, Book, Library, Librarian
from .models import Book
# Query 1: All books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

#from .models import Book  # Assuming the model name is 'Book' and it has an 'author' field

def filter_books_by_author(author):
    books_by_author = Book.objects.filter(author=author)
    return books_by_author

# relationship_app/query_samples.py

#from relationship_app.models import Librarian, Library

# Example: Query to find the librarian for a specific library
library_name = "Central Library"  # Change this to the name of the library you want
library = Library.objects.get(name=library_name)

# Retrieve the librarian for this library
librarian = Librarian.objects.get(library=library)

# Print out the librarian's details
print(f"Librarian for {library.name}: {librarian.name}")
