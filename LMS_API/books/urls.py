from django.urls import path, include
from .views import BookViewSet, AuthorViewSet, BorrowRecordView, ReturnRecordView, BookBorrowHistoryView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:book_id>/borrow', BorrowRecordView.as_view(), name='book-borrow'),
    path('books/return/<int:book_id>/', ReturnRecordView.as_view(), name='book-return'),
    path('books/history/', BookBorrowHistoryView.as_view(), name='book-borrow-history'),
]
