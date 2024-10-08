from rest_framework import serializers
from django.conf import settings
from rest_framework import serializers
from .models import Book, BorrowRecord, Author
#books Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#book borrowing serializer

#Authors 
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
class BookBorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id', 'user', 'book', 'checkout_date', 'return_date']
        
class BookReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = ['id', 'return_date']
        

class BookBorrowSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BorrowRecord
        fields = ['book_title', 'user_name', 'checkout_date', 'return_date']
