from django.urls import path
from . import  views
from .views import list_books
from .views import register_view, login_view, logout_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view
views.register
urlpatterns = [
    path('books/', views.list_books, name='list_books'), 
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  
]


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

urlpatterns = [
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
]

urlpatterns = [
    path('add_book/', views.add_book_view, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book_view, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book_view, name='delete_book'),
]