from django.urls import path
from .views import BookListView
url_patterns = [
    path("",BookListView, name = 'list')
]

