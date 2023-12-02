from django.db import models
from .consts import MAX_RATE, CATEGORY


# 評価の選択肢を定義（0からMAX_RATEまで）
RATE_CHOICES = [(x, str(x)) for x in range(0, MAX_RATE + 1)]


class Book(models.Model):
    """
    本に関する情報を格納するためのモデル。

    Attributes:
        title (models.CharField): 本のタイトル。
        text (models.TextField): 本の説明や内容。
        thumbnail (models.ImageField): 本のサムネイル画像。
        category (models.CharField): 本のカテゴリー。
        url (models.URLField): 本の詳細情報へのURL。
        user (models.ForeignKey): 本を登録したユーザーへの外部キー。
        views (models.PositiveIntegerField): 本が閲覧された回数。
    """

    title = models.CharField(max_length=100)
    text = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    本のレビュー情報を格納するためのモデル。

    Attributes:
        book (models.ForeignKey): レビュー対象の本への外部キー。
        title (models.CharField): レビューのタイトル。
        text (models.TextField): レビューの詳細テキスト。
        rate (models.IntegerField): 本への評価。
        user (models.ForeignKey): レビューを登録したユーザーへの外部キー。
    """

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
