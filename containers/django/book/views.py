from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.db.models.manager import BaseManager
from django.core.exceptions import PermissionDenied
from django.db.models import F
from django.urls import reverse
from .models import Book, Review
from .forms import BookForm, ReviewForm
from typing import Optional, Final


def index_book_view(request: HttpRequest, user: Optional[str] = None) -> HttpResponse:
    """
    レビューに基づいて本のリストとランキングを表示します。

    ユーザー名が提供されている場合は、そのユーザーの本をフィルタリングして表示します。そうでない場合は、すべての本を表示します。
    各本に平均評価とレビュー数を注釈として付けます。

    Args:
        request: HttpRequestオブジェクト。
        user: 表示するユーザーのユーザー名（任意）。

    Returns:
        本のリストとレビューランキングをレンダリングしたHttpResponse。
    """
    if user:
        base_queryset: BaseManager[Book] = Book.objects.filter(user__username=user)
        if not base_queryset:
            raise Http404
    else:
        base_queryset: BaseManager[Book] = Book.objects.all()

    index_book_list: Final[BaseManager[Book]] = base_queryset.order_by("-id")
    review_ranking: Final[BaseManager[Book]] = base_queryset.order_by(
        (F("review_avg").desc(nulls_last=True))
    )

    return render(
        request,
        "book/index.html",
        {"index_book_list": index_book_list, "review_ranking": review_ranking},
    )


def detail_book_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    主キーによって特定の本の詳細ページを表示します。

    本の閲覧数を増やし、変更を保存します。

    Args:
        request: HttpRequestオブジェクト。
        pk: 表示する本の主キー。

    Returns:
        本の詳細ページをレンダリングしたHttpResponse。
    """
    book: Final[Book] = get_object_or_404(Book, pk=pk)
    book.views_increment()
    return render(request, "book/book_detail.html", {"item": book})


@login_required
def create_book_view(request: HttpRequest) -> HttpResponse:
    """
    新しい本のインスタンスを作成します。

    リクエストメソッドがPOSTであり、フォームが有効な場合、現在のユーザーに関連付けられた新しい本を保存します。

    Args:
        request: HttpRequestオブジェクト。

    Returns:
        作成に成功した場合はインデックスページへのリダイレクト、または本作成フォームを含むHttpResponse。
    """
    if request.method == "POST":
        form: BookForm = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.create_book(request)
            return redirect(reverse("index"))
    elif request.method == "GET":
        form: BookForm = BookForm()
    else:
        raise Http404
    return render(request, "book/book_create.html", {"form": form})


@login_required
def delete_book_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    主キーによって特定の本を削除します。

    本を作成したユーザーのみが削除できます。現在のユーザーが作成者でない場合はPermissionDeniedを発生させます。

    Args:
        request: HttpRequestオブジェクト。
        pk: 削除する本の主キー。

    Returns:
        削除に成功した場合はインデックスページへのリダイレクト、または本削除確認ページを含むHttpResponse。
    """
    book: Final[Book] = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        raise PermissionDenied
    if request.method == "POST":
        book.delete()
        return redirect(reverse("index"))
    elif request.method == "GET":
        return render(request, "book/book_delete.html", {"object": book})
    else:
        raise Http404


@login_required
def update_book_view(request: HttpRequest, pk: int) -> HttpResponse:
    """
    主キーによって特定の本を更新します。

    本を作成したユーザーのみが更新できます。現在のユーザーが作成者でない場合はPermissionDeniedを発生させます。
    フォームが有効な場合、本を更新し、本の詳細ビューへのリダイレクトを返します。

    Args:
        request: HttpRequestオブジェクト。
        pk: 更新する本の主キー。

    Returns:
        更新に成功した場合は本の詳細ページへのリダイレクト、または本更新フォームを含むHttpResponse。
    """
    book: Final[Book] = get_object_or_404(Book, pk=pk)
    if book.user != request.user:
        raise PermissionDenied
    form: Final[BookForm] = BookForm(
        request.POST or None, request.FILES or None, instance=book
    )
    if form.is_valid():
        form.save()
        return redirect(reverse("detail-book", kwargs={"pk": pk}))
    return render(request, "book/book_update.html", {"form": form})


@login_required
def create_review_view(request: HttpRequest, book_id: int) -> HttpResponse:
    """
    特定の本に対するレビューを作成します。

    フォームが有効であれば、本と現在のユーザーに関連付けられたレビューを保存します。

    Args:
        request: HttpRequestオブジェクト。
        book_id: レビューを作成する本の主キー。

    Returns:
        レビュー作成に成功した場合は本の詳細ページへのリダイレクト、またはレビュー作成フォームを含むHttpResponse。
    """
    book: Final[Book] = get_object_or_404(Book, pk=book_id)
    form: Final[ReviewForm] = ReviewForm(request.POST or None)
    if form.is_valid():
        form.create_review(request, book)
        return redirect(reverse("detail-book", kwargs={"pk": book_id}))
    return render(request, "book/review_form.html", {"form": form})
