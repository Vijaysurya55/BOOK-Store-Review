# reviews/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField()

    def __str__(self):
        return f"Review of '{self.book.title}'"