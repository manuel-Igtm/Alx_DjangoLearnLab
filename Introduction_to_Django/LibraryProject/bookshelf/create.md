# Create Operation

## Command
```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_date=1949)
book.save()

Expected Output 
#No ouput is expected, but the book is created successfully
