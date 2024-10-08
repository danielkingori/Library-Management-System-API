from django.shortcuts import render
from .models import Book, Author, BorrowRecord
from rest_framework import generics, viewsets
from .serializers import BookSerializer, AuthorSerializer, BookBorrowSerializer, BookReturnSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, request
from django.utils import timezone



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BorrowRecordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        
        #check if the book is available
        if book.number_of_copies_available < 1:
            return Response({"error": "No available copies of the book"}, status=status.HTTP_400_BAD_REQUEST)
        
        #check fi the user already checkedout this book
        
        if BorrowRecord.objects.filter(user=request.user, book=book, return_date__isnull=True).exists():
            return Response({"error": "you have alreadyc hecked out this book"}, status=status.HTTP_400_BAD_REQUEST)
        
        #create a new checkout entry
        checkout = BorrowRecord.objects.create(user=request.user, book=book)
        
        # Reduce the number of available copies
        book.number_of_copies_available -= 1
        book.save()
        
        serializer = BookBorrowSerializer(checkout)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class ReturnRecordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, checkout_id):
        try:
            checkout = BorrowRecord.objects.get(id=checkout_id, user=request.user, return_date__isnull=True)
        except BorrowRecord.DoesNotExist:
            return Response({"error": "No active checkout found for this book."}, status=status.HTTP_400_BAD_REQUEST)

        # Mark the book as returned
        checkout.return_date = timezone.now()
        checkout.save()

        # Increase the number of available copies
        book = checkout.book
        book.number_of_copies_available += 1
        book.save()

        serializer = BookReturnSerializer(checkout)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
class BookBorrowHistoryView(generics.ListAPIView):
    serializer_class = BookBorrowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Optionally, filter to show only checkouts for the current user
        user = self.request.user
        return BorrowRecord.objects.filter(user=user).order_by('-borrow_date')