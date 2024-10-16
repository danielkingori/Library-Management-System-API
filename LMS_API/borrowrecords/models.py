from django.db import models
from django.conf import settings
from django.utils import timezone
from books.models import Book, Author

# BorrowRecord to record Borrow and Return of Books.
class BorrowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)  # Automatically set when borrowed
    due_date = models.DateField() 
    return_date = models.DateField(null=True, blank=True)  # Return date, allows null if not returned
    returned = models.BooleanField(default=False) #track if the book has been returned

    #to ensure that a user can not be associated with the same book twice
    class Meta:
        unique_together = ('user', 'book')

    @property
    def status(self):
        # If return_date is None, it means the book is still borrowed
        if self.return_date is None:
            today = timezone.now().date()
            if today > self.due_date:  # Check if it's overdue
                return "Overdue"
            return "Currently Borrowed"
        
        return "Returned"  # If return_date is set, it means the book has been returned

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"