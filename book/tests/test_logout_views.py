from django.urls import reverse
from ..models import Book, Review
from .common_test import BookExistTestCase


class TestLogoutViews(BookExistTestCase):
    """
    ログアウト状態の本アプリのビューのテストクラス。
    """

    def setUp(self):
        super().setUp()
        self.client.logout()

    def test_read_book_success(self):
        """
        本の閲覧が成功することを検証します。
        """
        response = self.client.get(
            reverse("detail-book", kwargs={"pk": self.my_book.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_read_not_exist_book_failure(self):
        """
        存在しない本の閲覧が失敗することを検証します。
        """
        response = self.client.get(reverse("detail-book", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, 404)

    def test_create_book_not_login_failure(self):
        """
        非ログイン状態で本の作成が失敗することを検証します。
        """
        params = {
            "title": "New Book",
            "text": "New text content",
            "category": "mobile",
            "thumbnail": "",
            "url": "https://example.com",
        }
        response = self.client.post(reverse("create-book"), params)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(title="New Book").exists())

    def test_update_book_not_login_failure(self):
        """
        非ログイン状態で本の更新が失敗することを検証します。
        """
        params = {
            "title": "Updated Book",
            "text": "Updated text content",
            "category": self.my_book.category,
            "thumbnail": "",
            "url": "https://example.com",
        }
        response = self.client.post(
            reverse("update-book", kwargs={"pk": self.my_book.pk}), params
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Book.objects.filter(
                title="Updated Book", text="Updated text content"
            ).exists()
        )

    def test_delete_book_not_login_failure(self):
        """
        非ログイン状態で本の削除が失敗することを検証します。
        """
        response = self.client.post(
            reverse("delete-book", kwargs={"pk": self.my_book.pk})
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(pk=self.my_book.pk).exists())

    def test_create_review_not_login_failure(self):
        """
        非ログイン状態でレビューの作成が失敗することを検証します。
        """
        params = {
            "title": "New Review",
            "text": "New review content",
            "rate": 5,
        }
        response = self.client.post(
            reverse("review", kwargs={"book_id": self.my_book.pk}), params
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Review.objects.filter(title="New Review").exists())
