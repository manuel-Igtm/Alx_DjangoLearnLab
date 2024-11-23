from .views import Booklist
from django.urls import path

urlpatterns = [
    path("api/books", Booklist.as_view(), name = "book_lists"),
]
