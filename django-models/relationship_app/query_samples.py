from relationship_app.models import Author, Book, Library, Librarian

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

# Example: Query to find all books by a specific author
author_name = "J.K. Rowling"  # You can change this to any author name
author = Author.objects.get(name=author_name)

books_by_author = Book.objects.filter(author=author)  # Correct filter usage

# Print out the books by this author
for book in books_by_author:
    print(f"Book Title: {book.title}, Author: {book.author.name}")

    # Example: Query to find the librarian for a specific library
library_name = "Central Library"  # Change this to the name of the library you want
library = Library.objects.get(name=library_name)

# Retrieve the librarian for this library
librarian = Librarian.objects.get(library=library)

# Print out the librarian's details
print(f"Librarian for {library.name}: {librarian.name}")