from django.shortcuts import render
from .models import Book, Author
from rest_framework import viewsets, status, permissions
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.decorators import api_view
from .filters import BookFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination


class IsAdmin(permissions.BasePermission):
   
    def has_permission(self, request, view):
        # Allow GET (read-only) requests for everyone (admins and members)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Only allow non-safe methods (POST, PUT, DELETE) for Admins
        return request.user.is_authenticated and request.user.role == 'admin'

class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = CustomPagination
    
    # Override the get_permissions method
    def get_permissions(self):
        # Apply IsAdmin permission only to unsafe methods (POST, PUT, DELETE)
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        # Otherwise, allow any user to view authors
        return super().get_permissions()     
    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter
    pagination_class = CustomPagination
    
     # Override the get_permissions method
    def get_permissions(self):
        # Apply IsAdmin permission only to unsafe methods (POST, PUT, DELETE)
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        # Otherwise, allow any user to view books
        return super().get_permissions()

