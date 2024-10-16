from rest_framework import serializers
from django.conf import settings
from rest_framework import serializers
from .models import Book, Author
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

