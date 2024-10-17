from django.urls import path, include
from .views import borrow_history, borrow_book, return_book



urlpatterns = [
    path('borrow/', borrow_book, name='borrow-book'),
    path('return/', return_book, name='return-book'),
    path('return/<int:book_id>/', return_book, name='return-book'),
    path('history/', borrow_history, name='borrowing-history'),
]
