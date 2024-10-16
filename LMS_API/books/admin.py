from django.contrib import admin
from .models import Author, Book
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookAdmin(admin.ModelAdmin):
    def author(self, obj):
        return obj.author.name
    
    list_display = ('title','author', 'isbn', 'published_date', 'number_of_copies_available')



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)