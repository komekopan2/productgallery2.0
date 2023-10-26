from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Book, Review
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE
from django.views import generic

# from .forms import CreateBookForm
import os

# Create your views here.

# q:このファイルは何？
# a:ビューを定義するためのファイル
# q:ビューとは何？
# a:ユーザーからのリクエストを受け取り、レスポンスを返す関数
# q:ビューを定義するためには、どのように記述する？
# a:関数を作成する
# q:ビューの関数の引数は何がある？
# a:リクエストオブジェクト
# q:リクエストオブジェクトとは何？
# a:ユーザーからのリクエストに関する情報を持つオブジェクト
# q:リクエストオブジェクトの中身はどのように確認する？
# a:print(request)で確認する
# q:リクエストオブジェクトの中身はどのように使う？
# a:リクエストオブジェクト.属性名で使う


class ListBookView(LoginRequiredMixin, ListView):
    template_name = "book/book_list.html"
    # htmlファイルで↓のモデルの中身が使いまわされる
    model = Book
    paginate_by = ITEM_PER_PAGE


class DetailBookView(LoginRequiredMixin, DetailView):
    template_name = "book/book_detail.html"
    model = Book

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        obj.views += 1
        obj.save()

        return obj


class CreateBookView(LoginRequiredMixin, CreateView):
    template_name = "book/book_create.html"
    model = Book
    fields = {"title", "text", "category", "thumbnail", "url"}
    success_url = reverse_lazy("index")
    # form_class = CreateBookForm

    def form_valid(self, form):
        # ユーザー情報の追加をする関数
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteBookView(LoginRequiredMixin, DeleteView):
    template_name = "book/book_delete.html"
    model = Book
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj


class UpdateBookView(LoginRequiredMixin, UpdateView):
    template_name = "book/book_update.html"
    model = Book
    fields = {"title", "text", "category", "thumbnail", "url"}
    # success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj

    def get_success_url(self):
        return reverse("detail-book", kwargs={"pk": self.object.id})


class CreateReviewView(LoginRequiredMixin, CreateView):
    template_name = "book/review_form.html"
    model = Review
    fields = {"book", "title", "text", "rate"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = Book.objects.get(pk=self.kwargs["book_id"])
        # print(context)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail-book", kwargs={"pk": self.object.book.id})


class IndexBookView(ListView):
    template_name = "book/index.html"
    # htmlファイルで↓のモデルの中身が使いまわされる
    model = Book
    context_object_name = "object_list"

    def get_context_data(self, **kwargs):
        context = super(IndexBookView, self).get_context_data(**kwargs)
        context.update(
            {
                # さらにテンプレートに載せたいモデルがあれば下記に追記
                # テンプレートで使う変数:querysetオブジェクト
                "ranking_list": Book.objects.annotate(
                    avg_rating=Avg("review__rate")
                ).order_by("-avg_rating")
            }
        )
        return context

    def get_queryset(self):
        return Book.objects.order_by("-id")


""" 
def index_view(request):
    object_list = Book.objects.order_by("-id")
    ranking_list = Book.objects.annotate(
        avg_rating=Avg("review__rate")).order_by("-avg_rating")

    # paginator = Paginator(ranking_list, ITEM_PER_PAGE)
    # page_number = request.GET.get('page', 1)
    # page_obj = paginator.page(page_number)
    
    return render(request, "book/index.html", {"object_list": object_list, "ranking_list": ranking_list,})

 """
# def logout_view(request):
#     logout(request)
#     return redirect("index")  # success_url
