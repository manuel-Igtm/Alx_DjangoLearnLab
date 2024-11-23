from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class BookList(generics.ListAPIView, APIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return Response({'message': 'Hello authenticated user'})



class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return Response({'message': 'Hello authenticated user'})


    