from django.contrib import admin
from .models import BorrowRecord
# Register your models here.

class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrow_date', 'return_date', 'status')
    
admin.site.register(BorrowRecord, BorrowRecordAdmin)