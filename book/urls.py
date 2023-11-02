from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index_view, name="index"),
    path("", views.index_book_view, name="index"),
    path("book/<int:pk>/", views.detail_book_view, name="detail-book"),
    path("book/create/", views.create_book_view, name="create-book"),
    path("book/<int:pk>/delete/", views.delete_book_view, name="delete-book"),
    path("book/<int:pk>/update/", views.update_book_view, name="update-book"),
    path("book/<int:book_id>/review/", views.create_review_view, name="review"),
]
