from django.urls import path
from .views import BookListView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

url_patterns = [
    path("", BookListView, name = 'list'),
    path("", SignUpView, name = 'signup'),
    path("views.register", LoginView.as_view(template_name='registration/login.html', name = 'login')),
    path("views.register", LogoutView.as_view(template_name='registration/logout.html', name = 'logout')),
]


