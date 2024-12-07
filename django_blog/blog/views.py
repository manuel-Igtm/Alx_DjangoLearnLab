from django.shortcuts import render, redirect
from .models import User,Post
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUser
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class HomeView(TemplateView):
    template_name = "blog/base.html"


def register(request):
    if request.method == 'POST':
        form =  CustomUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('profile')
        else:
            form = CustomUser()
    return render(request, 'blog/register.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'blog/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        request.user.email = request.POST['email']
        request.user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html')       
