from django.contrib import admin
from .models import Author, Book, BorrowRecord
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'published_date', 'number_of_copies_available')

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)