from django.db import models
from django.conf import settings


# AuthorModel with Name and biography fields
class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name

#BookModel with following fields:Title of the book, Author of the book, ISBN number (should be unique), Date the book was published, Number of copies available
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    number_of_copies_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

#BorrowRecord with the Check-Out and Return Books.
class BorrowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowing {self.book.title}"

