from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Book, Review
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from .forms import BookForm, ReviewForm
from django.db.models import Avg, Case, When, Value, IntegerField, Count


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
    index_book_list = Book.objects.annotate(
        avg_rating=Avg("review__rate"), review_count=Count("review")
    ).order_by("-id")

    review_ranking = Book.objects.annotate(
        avg_rating=Avg("review__rate"),
        review_count=Count("review"),
        # 以下のCase Whenはavg_ratingがNULLでない場合は1、そうでない場合は0をrating_existsに格納
        rating_exists=Case(
            When(review__rate__isnull=False, then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        ),
    ).order_by(
        "-rating_exists",
        "-avg_rating",
        "-review_count",  # まずはレビューが存在するかどうかで並べ替え、次に平均レーティング、レビュー数の順で並べ替え
    )

    return render(
        request,
        "book/index.html",
        {"index_book_list": index_book_list, "review_ranking": review_ranking},
    )
