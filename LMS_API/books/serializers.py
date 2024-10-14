from rest_framework import serializers
from django.conf import settings
from rest_framework import serializers
from .models import Book, BorrowRecord, Author
from datetime import date


#Authors 
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'



#books Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookBorrowSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_author = serializers.CharField(source='book.author', read_only=True)
    borrow_date = serializers.DateField(format="%Y-%m-%d", read_only=True)
    due_date = serializers.DateField(format="%Y-%m-%d") 

    class Meta:
        model = BorrowRecord
        fields = ['book_title', 'book_author', 'borrow_date', 'due_date']

    def validate_due_date(self, value):
        #Ensure due date is in the correct format and is valid
        if value is None:
            return value
        
        # Check if value is a string
        if isinstance(value, str):
            try:
                # Convert from string to date
                return serializers.DateField().to_internal_value(value)
            except serializers.ValidationError:
                raise serializers.ValidationError("Due date must be in YYYY-MM-DD format.")
        
        # Check if value is already a date object
        if isinstance(value, (date)):  # Ensuring both date and datetime are handled
            return value
        
        # Raise an error if the value is neither a valid string nor a date object
        raise serializers.ValidationError("Due date must be a string or None")


#book return serializer
class BookReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['book_id']
        
# class BookReturnSerializer(serializers.ModelSerializer):
#     book_id = serializers.IntegerField()
    
#     class Meta:
#         model = BorrowRecord
#         fields = 'id'

#     def validate_book_id(self, value):
#         # You can add any additional validation for book_id here if needed
#         if value <= 0:
#             raise serializers.ValidationError("Book ID must be a positive integer.")
#         return value


#borrow history serializer
class BorrowHistorySerializer(serializers.ModelSerializer):
    book_id = serializers.CharField(source='book.id', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)
    book_author = serializers.CharField(source='book.author', read_only=True)
    date_borrowed =  serializers.DateField(source='borrow_date', read_only=True)
    date_due = serializers.DateField(source='due_date', read_only=True)
    date_returned = serializers.DateField(source='return_date', allow_null=True)
    book_status = serializers.CharField(source='status', read_only=True)

    class Meta:
        model = BorrowRecord
        fields = ['book_id','book_title','book_author', 'book_status', 'date_borrowed', 'date_returned', 'date_due']