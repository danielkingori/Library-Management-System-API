from django.shortcuts import render
from .models import Book, Author, BorrowRecord
from rest_framework import generics, viewsets, status, permissions
from .serializers import BookSerializer, AuthorSerializer, BookBorrowSerializer, BookReturnSerializer, BorrowHistorySerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, request
from django.utils import timezone
from rest_framework.decorators import api_view



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
# class BorrowRecordView(APIView):
#     permission_classes = [IsAuthenticated]
    
#     def post(self, request, book_id):
#         book = Book.objects.get(id=book_id)
        
#         #check if the book is available
#         if book.number_of_copies_available < 1:
#             return Response({"error": "No available copies of the book"}, status=status.HTTP_400_BAD_REQUEST)
        
#         #check fi the user already checkedout this book
        
#         if BorrowRecord.objects.filter(user=request.user, book=book, return_date__isnull=True).exists():
#             return Response({"error": "you have already checked out this book"}, status=status.HTTP_400_BAD_REQUEST)
        
#         #create a new checkout entry
#         checkout = BorrowRecord.objects.create(user=request.user, book=book)
        
#         # Reduce the number of available copies
#         book.number_of_copies_available -= 1
#         book.save()
        
#         serializer = BookBorrowSerializer(checkout)
#         return Response({"message": "Book borrowed successfully."}, status=status.HTTP_201_CREATED)
    

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
        return Response({"message": "Book returned successfully."}, status=status.HTTP_200_OK)
        
            


@api_view(['POST'])
def borrow_book(request):
    serializer = BookBorrowSerializer(data=request.data)

    if serializer.is_valid():
        book_id = request.data.get('book_id')  # Get the book ID from the request
        try:
            book = Book.objects.get(id=book_id)

            # Check if the book is available
            if book.number_of_copies_available <= 0:
                return Response({"error": "No available copies."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the user already has the book borrowed
            existing_borrow_record = BorrowRecord.objects.filter(user=request.user, book=book)
            if existing_borrow_record.exists():
                return Response({"error": "You have already borrowed this book."}, status=status.HTTP_400_BAD_REQUEST)

            # Create a new BorrowRecord
            borrow_record = BorrowRecord.objects.create(
                book=book,
                user=request.user,  # Assuming you set user during borrowing
                # return_date=serializer.validated_data['return_date'],
                borrow_date=timezone.now()  # Set current date as the checkout date
            )

            # Reduce the available copies
            book.number_of_copies_available -= 1
            book.save()

            return Response(BookBorrowSerializer(borrow_record).data, status=status.HTTP_201_CREATED)

        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class BorrowHistoryView(generics.ListAPIView):
    serializer_class = BorrowHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter the borrow records for the authenticated user
        return BorrowRecord.objects.filter(user=self.request.user).order_by('-borrow_date')
    
@api_view(['POST'])
def return_book(request):
    serializer = BookReturnSerializer(data=request.data)

    if serializer.is_valid():
        # book_id = serializer.validated_data['book_id']
        book_id = request.data.get('book_id') 
        
        try:
            # Retrieve the user's borrow record for the specific book
            borrow_record = BorrowRecord.objects.get(user=request.user, book_id=book_id)

            # Ensure that the return_date is not None
            if borrow_record.return_date is None:
                return Response({"error": "Return date is not set."}, status=status.HTTP_400_BAD_REQUEST)

            # Calculate fine if the book is returned past the due date
            today = timezone.now().date()
            if today > borrow_record.return_date:
                overdue_days = (today - borrow_record.return_date).days
                fine = overdue_days * 1  # Charge $1 per day overdue
            else:
                fine = 0  # No fine if returned on time

            # Increase available copies of the book after successful return
            book = borrow_record.book
            book.number_of_copies_available += 1
            book.save()  # Save updated available copies

            # Delete the borrow record since the book has been returned
            borrow_record.delete()

            # Prepare a response indicating success and any fine charged
            return Response({
                "message": "Book returned successfully.",
                "fine": f"${fine:.2f}"
            }, status=status.HTTP_200_OK)


        except BorrowRecord.DoesNotExist:
            return Response({"error": "No borrow record found for this book."}, status=status.HTTP_404_NOT_FOUND)
        
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)