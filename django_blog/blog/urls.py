from .views import HomeView, RegisterView, ProfileView
from django.urls import path
from . import views


urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
