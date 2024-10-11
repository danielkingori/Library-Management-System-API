from django.urls import path, include
from .views import BookViewSet, AuthorViewSet, ReturnRecordView, BorrowHistoryView, borrow_book, return_book
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('books/<int:book_id>/borrow', BorrowRecordView.as_view(), name='book-borrow'),
    path('books/return/<int:checkout_id>', ReturnRecordView.as_view(), name='book-return'),
    path('borrow/', borrow_book, name='borrow-book'),
    path('borrowing-history/', BorrowHistoryView.as_view(), name='borrowing-history'),
    path('return-book/', return_book, name='return-book'),
]
