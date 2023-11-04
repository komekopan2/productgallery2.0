from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from django.urls import reverse
from django.db.models import Avg
from django.core.exceptions import PermissionDenied
from .forms import BookForm, ReviewForm


@login_required
def detail_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.views += 1
    book.save()
    return render(request, "book/book_detail.html", {"object": book})


@login_required
def create_book_view(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect(reverse("index"))
    else:
        form = BookForm()
    return render(request, "book/book_create.html", {"form": form})


@login_required
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        raise PermissionDenied
    if request.method == "POST":
        book.delete()
        return redirect(reverse("index"))
    return render(request, "book/book_delete.html", {"object": book})


@login_required
def update_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        raise PermissionDenied
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect(reverse("detail-book", kwargs={"pk": pk}))
    return render(request, "book/book_update.html", {"form": form})


@login_required
def create_review_view(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        review = form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect(reverse("detail-book", kwargs={"pk": book_id}))
    return render(request, "book/review_form.html", {"form": form})


def index_book_view(request):
    books = Book.objects.order_by("-id")
    ranking_list = Book.objects.annotate(avg_rating=Avg("review__rate")).order_by(
        "-avg_rating"
    )
    return render(
        request, "book/index.html", {"object_list": books, "ranking_list": ranking_list}
    )
