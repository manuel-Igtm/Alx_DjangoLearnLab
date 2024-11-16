from django.shortcuts import render , redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .models import Library
from django.contrib import messages



# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.all()    
        context['books'] = book

def list_books(request):
    # list of all book instances
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def LogoutView(request):
    return render(request, 'logout.html')


def LoginView(request):
    return render(request, 'login.html')


def Register(request):
    return render(request, 'register.html')

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, "Account created successfully!")
            # Redirect to login page after registration
            return redirect('login')
    else:
        form = UserCreationForm()  # Display an empty form for GET requests

    return render(request, 'relationship_app/register.html', {'form': form})