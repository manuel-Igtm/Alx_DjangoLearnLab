from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .serializers import BookSerializer 
from models import Book
# Create your views here.

class BookListView(generic.ListView):
    """
    View to list all books
    """
    model = Book
    template_name = 'book_list.html' #Specify your template
    context_object_name = 'books' #Context variable name for the list of books

class BookDetailView(generic.DetailView):
    #view to retrieve a single book by ID

    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

class BookCreateView(generic.CreateView):

    model = Book 
    template_name = 'book_form.html'
    fields = ['title','author','published_date']
    success_url= reverse_lazy('book-list')

class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'book_form.html'
    fields = ['title','author','published_date']
    success_url = reverse_lazy('book-list')

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
