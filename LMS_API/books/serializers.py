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
    
    author_name = serializers.SerializerMethodField()
    
    # Method to get the author's name
    def get_author_name(self, obj):
        return obj.author.name 
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'published_date', 'number_of_copies_available', 'author_name']

