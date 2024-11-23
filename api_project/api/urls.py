from .views import BookList, BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')



urlpatterns = [
    path("api/books", BookList.as_view(), name = "book_lists"),
    path('api/', include(router.urls)),
]
