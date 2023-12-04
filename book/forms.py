from django import forms
from .models import Book, Review
from django.http import HttpRequest
from typing import Final


class BookForm(forms.ModelForm):
    """
    Bookモデルのデータ入力用のフォームを作成するためのクラス。

    ModelFormを継承しており、具体的にはBookモデルのインスタンスを
    作成または更新するために使用されます。

    Attributes:
        model: Bookモデルがフォームの操作対象となります。
        fields (list[str]): フォームに表示されるフィールドのリスト。
            'title', 'text', 'category', 'thumbnail', 'url' を含みます。
    """

    def create_book(self, request: HttpRequest) -> None:
        """
        フォームの入力をもとにBookモデルのインスタンスを作成します。

        Args:
            request: HttpRequestオブジェクト。
        """
        book: Final[Book] = self.save(commit=False)
        book.user = request.user
        book.save()

    class Meta:
        model = Book
        fields = ["title", "text", "category", "thumbnail", "url"]


class ReviewForm(forms.ModelForm):
    """
    Reviewモデルのデータ入力用のフォームを作成するためのクラス。

    ModelFormを継承しており、具体的にはReviewモデルのインスタンスを
    作成または更新するために使用されます。

    Attributes:
        model: Reviewモデルがフォームの操作対象となります。
        fields (list[str]): フォームに表示されるフィールドのリスト。
            'title', 'text', 'rate' を含みます。
    """

    def create_review(self, request: HttpRequest, book: Book) -> None:
        """
        フォームの入力をもとにReviewモデルのインスタンスを作成します。

        Args:
            request: HttpRequestオブジェクト。
            book: レビュー対象の本のインスタンス。
        """
        review: Final[Review] = self.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        book.review_recache()

    class Meta:
        model = Review
        fields = ["title", "text", "rate"]
