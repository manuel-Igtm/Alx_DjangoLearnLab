from django.urls import path
from .views import BookListView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

url_patterns = [
    path("", BookListView, name = 'list'),
    path("", SignUpView, name = 'signup'),
    path("", LoginView, name = 'login'),
    path("", LogoutView, name = 'logout'),
]


