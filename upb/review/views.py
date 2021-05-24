"""
views
"""
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Book
from .models import Review
from .forms import ReviewForm

# Create your views here.

def index(request):
    """
    review index:
    Show all the books
    """
    books = Book.objects.all()
    context = dict(books=books)
    return render(request, 'review/index.html', context)

def book_detail(request, book_id):
    """
    Show book's details and a form to submit a review.
    """
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
           review = Review(book=book, review=form.cleaned_data['review_text'])
           review.save()
           return HttpResponseRedirect('/review/')
    else:
        form = ReviewForm()
    context = dict(book=book, form=form)
    return render(request, 'review/book_detail.html', context)
