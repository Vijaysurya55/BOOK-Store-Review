
from django.shortcuts import render, redirect
from .models import Book, Review

def add_review(request):
    if request.method == 'POST':
        book_title = request.POST['book_title']
        review_text = request.POST['review_text']

        book, created = Book.objects.get_or_create(title=book_title)
        Review.objects.create(book=book, review_text=review_text)

        return redirect('display_reviews')

    return render(request, 'reviews/add_review.html')

def display_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/display_reviews.html', {'reviews': reviews})
