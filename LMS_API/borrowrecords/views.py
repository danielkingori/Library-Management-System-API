from django.shortcuts import render
from .models import BorrowRecord
from books.models import Book
from rest_framework import status
from .serializers import BookBorrowSerializer, BookReturnSerializer, BorrowHistorySerializer
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import api_view



#book borrow view
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

            # Check if the user already has the book borrowed, or already returned
            existing_borrow_record = BorrowRecord.objects.filter(user=request.user, book=book, return_date__isnull=True)
            
            if existing_borrow_record.exists():
                return Response({"error": "You have already borrowed this book and not yet returned it."}, status=status.HTTP_400_BAD_REQUEST)

            borrow_record = BorrowRecord.objects.create(
                book=book,
                user=request.user,  # access the set user during borrowing based on access token
                borrow_date=timezone.now(),  # Set current date as the borrow date
                due_date=serializer.validated_data['due_date'],
            )

            # Reduce the available copies
            book.number_of_copies_available -= 1
            book.save()

            return Response(BookBorrowSerializer(borrow_record).data, status=status.HTTP_201_CREATED)

        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#book return view
@api_view(['POST'])
def return_book(request, book_id):
    serializer = BookReturnSerializer(data=request.data)

    if serializer.is_valid():
        try:
            # Retrieve the borrow record for the specific book that is currently borrowed
            borrow_record = BorrowRecord.objects.get(user=request.user, book_id=book_id, returned=False)
            
            # Mark the book as returned
            borrow_record.returned = True  
            borrow_record.return_date = timezone.now().date()

            # Calculate fine if the book is returned past the due date
            if borrow_record.return_date > borrow_record.due_date:
                overdue_days = (borrow_record.return_date - borrow_record.due_date).days
                fine = overdue_days * 1  # Charge $1 per day overdue
            else:
                fine = 0  # No fine if returned on time

            # Increase available copies of the book after successful return
            book = borrow_record.book
            book.number_of_copies_available += 1
            book.save()  # Save updated available copies

            # Save the borrow record to update the return date
            borrow_record.save()

            # Prepare a response indicating success and any fine charged
            return Response({
                "message": "Book returned successfully.",
                "fine": f"${fine:.2f}, for exceeding the due date by {overdue_days} days" if fine else "No fine."
            }, status=status.HTTP_200_OK)

        except BorrowRecord.DoesNotExist:
            return Response({"error": "No borrow record found for this book."}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#maintaning the history of each borrow & return record
@api_view(['GET'])
def borrow_history(request):
    try:
        # Retrieve all borrow records for the user with related book information
        borrow_records = BorrowRecord.objects.filter(user=request.user).select_related('book')

        # Serialize the records
        serializer = BorrowHistorySerializer(borrow_records, many=True)

        # Return serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    except BorrowRecord.DoesNotExist:
        return Response({"error": "No borrow records found."}, status=status.HTTP_404_NOT_FOUND)
