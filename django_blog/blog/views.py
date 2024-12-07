from django.shortcuts import render, redirect
from .models import User,Post,Profile
from django.views.generic import TemplateView,CreateView,DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUser
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = "blog/base.html"

class RegisterView(CreateView):
    template_name = 'blog/register.html'  
    form_class = CustomUser
    success_url = reverse_lazy('login')  

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        #Fetch the profile for the currently logged-in user
        return Profile.objects.get(user = self.request.user)


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
