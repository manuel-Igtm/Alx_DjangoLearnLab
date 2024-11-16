from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
#list_books.html

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.all()    
        context['books'] = book
        
