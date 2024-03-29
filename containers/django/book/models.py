from django.db import models
from .consts import MAX_RATE, CATEGORY
from django.db.models import Avg
from django.db.models.manager import BaseManager
from typing import Final


# 評価の選択肢を定義（0からMAX_RATEまで）
RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


class Book(models.Model):
    """
    本に関する情報を格納するためのモデル。

    Attributes:
        title (models.CharField): 本のタイトル。
        text (models.TextField): 本の説明や内容。
        category (models.CharField): 本のカテゴリー。
        thumbnail (models.ImageField): 本のサムネイル画像。
        url (models.URLField): 本の詳細情報へのURL。
        user (models.ForeignKey): 本を登録したユーザーへの外部キー。
        views (models.PositiveIntegerField): 本が閲覧された回数。
    """

    title = models.CharField(max_length=100, verbose_name="タイトル")
    text = models.TextField(verbose_name="説明")
    category = models.CharField(max_length=100, choices=CATEGORY, verbose_name="カテゴリー")
    thumbnail = models.ImageField(null=True, blank=True, verbose_name="サムネイル(任意)")
    url = models.URLField(null=True, blank=True, verbose_name="URL(任意)")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    review_avg = models.FloatField(null=True, default=None)
    review_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    def views_increment(self) -> None:
        """
        本の閲覧数を増やし、変更を保存します。
        """
        self.views += 1
        self.save()

    def review_recache(self) -> None:
        """
        レビューの平均値とレビュー数を再計算して保存します。
        """
        reviews: Final[BaseManager[Review]] = Review.objects.filter(book=self)
        self.review_avg = reviews.aggregate(Avg("rate"))["rate__avg"]
        self.review_count = reviews.count()
        self.save()


class Review(models.Model):
    """
    本のレビュー情報を格納するためのモデル。

    Attributes:
        book (models.ForeignKey): レビュー対象の本への外部キー。
        title (models.CharField): レビューのタイトル。
        text (models.TextField): レビュー内容。
        rate (models.IntegerField): 星の数。
        user (models.ForeignKey): レビューを登録したユーザーへの外部キー。
    """

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="タイトル")
    text = models.TextField(verbose_name="レビュー内容")
    rate = models.IntegerField(choices=RATE_CHOICES, verbose_name="星の数")
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
