from django.db import models


#Book Model with following fields:Title of the book, Author of the book, ISBN number (should be unique), Date the book was published, Number of copies available
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    number_of_copies_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title