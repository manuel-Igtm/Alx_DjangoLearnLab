from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login



# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.all()    
        context['books'] = book

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'



