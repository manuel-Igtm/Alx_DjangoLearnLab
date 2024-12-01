from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import BookSerializer 
from models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAuthenticated
#from django_filters import rest_framework
# Create your views here.

class ListView(generics.ListAPIView):
    """
    View to list all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # unauthenticated users can view
    filter_backends = (filters.SearchFilter,filters.OrderingFilter) # ordering and search filters
    ordering_fields = ['title', 'publication_year'] # order by title and publication year
    search_fields = ['title', 'author'] # search by title and author

class DetailView(generics.RetrieveAPIView):
    #view to retrieve a single book by ID
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # unauthenticated users can view

  

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # authenticated users only can create
    

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # authenticated users only can update
   
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] # authenticated users only can delete
   