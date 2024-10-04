from django.shortcuts import render
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer
# Create your views here.


class BookListCreate(generics.ListCreateAPIView):
    queryset =  Book.objects.all()
    serializer_class = BookSerializer