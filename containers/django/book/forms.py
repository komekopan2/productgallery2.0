from django import forms
from .models import Book, Review


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

    class Meta:
        model = Review
        fields = ["title", "text", "rate"]
