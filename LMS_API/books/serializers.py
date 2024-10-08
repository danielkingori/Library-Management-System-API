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