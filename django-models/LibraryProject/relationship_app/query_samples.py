from relationship_app.models import Author, Book, Librarian, Library

# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.

# relationship_app/query_samples.py

# from relationship_app.models import Book, Author, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")

# List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = Book.objects.all()
        print(f"Books in {library_name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

# Retrieve the librarian for a library
def retrieve_librarian(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"The librarian for {library_name} library is {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name} library")

# # Example usage
# if __name__ == "__main__":
#     # Change these to test with specific data
#     query_books_by_author('J.K. Rowling')
#     list_books_in_library('City Library')
#     retrieve_librarian('City Library')
