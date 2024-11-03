#Delete Operation

##Command 
``` python
#Delete the book instance
retrieved_book.delete()

#Confirm deletion by trying to retrieve the book
try:
    retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book has been deleted")

#Expected output
Book has been deleted 