from django.urls import path
from .views import BookListView, SignUpView,LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from django.contrib.auth import views
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

url_patterns = [
    path("", view=list_books, name='list_books'),
    path("", BookListView.as_view(template_name='relationship_app/list_books.html'), name = 'list'),
    path("", LibraryDetailView.as_view(template_name='relationship_app/library_detail.html'), name='library_detail'),
    path("", SignUpView, name = 'signup'),
    path("views.register", LoginView.as_view(template_name='relationship_app/login.html', name = 'login')),
    path("views.register", LogoutView.as_view(template_name='relationship_app/logout.html', name = 'logout')),
    path('register/', views.register, name ='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add_book/', add_book, name='add_book'),
    path('books/edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('', delete_book, name='delete_book')
]


