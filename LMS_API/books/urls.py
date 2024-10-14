from django.urls import path, include
from .views import BookViewSet, AuthorViewSet, borrow_history, borrow_book, return_book
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('borrow/', borrow_book, name='borrow-book'),
    path('return/', return_book, name='return-book'),
    path('return/<int:book_id>/', return_book, name='return-book'),
    path('history/', borrow_history, name='borrowing-history'),
]
