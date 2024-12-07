from .views import HomeView
from django.urls import path
from . import views


urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
