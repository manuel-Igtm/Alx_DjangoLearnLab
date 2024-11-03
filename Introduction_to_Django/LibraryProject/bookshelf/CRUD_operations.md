
### Step 3: Save All Commands and Outputs

Create a file named `CRUD_operations.md` and document all commands and expected outputs as follows:

```markdown
# CRUD Operations Documentation

## Create
```python
from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Retrieve the book you created
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

1984 George Orwell 1949


# Update the title of the book
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# No output is expected, but the title is updated successfully.

from bookshelf.models import Book

# Delete the book instance
retrieved_book.delete()

# Confirm deletion by trying to retrieve the book
try:
    Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book has been deleted.")

Book has been deleted.



