from django.urls import path
from . import views

"""
bookアプリケーションのURL設定を行うためのモジュール。

Attributes:
    app_name (str): アプリケーションの名前空間。
        この名前空間を利用して、URLの逆引きを行う。

    urlpatterns (list): URLのパターンのリスト。
        path関数を用いて、URLのパターンを追加する。
"""

urlpatterns = [
    path("", views.index_book_view, name="index"),
    path("filterby-user/<str:user>", views.index_book_view, name="filterby-user"),
    path("book/<int:pk>/", views.detail_book_view, name="detail-book"),
    path("book/create/", views.create_book_view, name="create-book"),
    path("book/<int:pk>/delete/", views.delete_book_view, name="delete-book"),
    path("book/<int:pk>/update/", views.update_book_view, name="update-book"),
    path("book/<int:book_id>/review/", views.create_review_view, name="review"),
]
