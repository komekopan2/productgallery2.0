from django.urls import reverse
from ..models import Book, Review
from .common_test import BookExistTestCase


class TestLoginViews(BookExistTestCase):
    """
    ログイン状態の本アプリのビューのテストクラス。
    """

    def test_create_book_success(self):
        """
        ログイン状態で本の作成が成功することを検証します。
        """
        params = {
            "title": "New Book",
            "text": "New text content",
            "category": "mobile",
            "thumbnail": "",
            "url": "https://example.com",
        }
        response = self.client.post(reverse("create-book"), params)
        self.assertRedirects(response, reverse("index"))
        self.assertTrue(
            Book.objects.filter(title="New Book", text="New text content").exists()
        )

    def test_create_missing_attributes_book_failure(self):
        """
        ログイン状態で必須属性が欠けた本の作成が失敗することを検証します。
        """
        params = {
            "title": "New Book2",
            "text": "",
            "category": "mobile",
            "thumbnail": "",
            "url": "https://example.com",
        }
        response = self.client.post(reverse("create-book"), params)
        self.assertFalse(Book.objects.filter(title="New Book2", text="").exists())

    def test_update_book_success(self):
        """
        ログイン状態で本の更新が成功することを検証します。
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
        self.assertRedirects(
            response, reverse("detail-book", kwargs={"pk": self.my_book.pk})
        )
        self.assertTrue(
            Book.objects.filter(
                title="Updated Book", text="Updated text content"
            ).exists()
        )

    def test_update_not_exist_book_failure(self):
        """
        ログイン状態で存在しない本の更新が失敗することを検証します。
        """
        params = {
            "title": "Updated Book2",
            "text": "Updated text content2",
            "category": self.my_book.category,
            "thumbnail": "",
            "url": "https://example.com",
        }
        response = self.client.post(reverse("update-book", kwargs={"pk": 999}), params)
        self.assertEqual(response.status_code, 404)
        self.assertFalse(
            Book.objects.filter(
                title="Updated Book2", text="Updated text content2"
            ).exists()
        )

    def test_update_other_user_book_failure(self):
        """
        ログイン状態で他ユーザーの本の更新が失敗することを検証します。
        """
        params = {
            "title": "Updated Book3",
            "text": "Updated text content3",
            "category": self.my_book.category,
            "thumbnail": "",
            "url": "https://example.com",
        }
        response = self.client.post(
            reverse("update-book", kwargs={"pk": self.other_book.pk}), params
        )
        self.assertEqual(response.status_code, 403)
        self.assertFalse(
            Book.objects.filter(
                title="Updated Book3", text="Updated text content3"
            ).exists()
        )

    def test_delete_book_success(self):
        """
        ログイン状態で本の削除が成功することを検証します。
        """
        response = self.client.post(
            reverse("delete-book", kwargs={"pk": self.my_book.pk})
        )
        self.assertRedirects(response, reverse("index"))
        self.assertFalse(Book.objects.filter(pk=self.my_book.pk).exists())

    def test_delete_not_exist_book_failure(self):
        """
        ログイン状態で存在しない本の削除が失敗することを検証します。
        """
        response = self.client.post(reverse("delete-book", kwargs={"pk": 999}))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Book.objects.filter(pk=self.my_book.pk).exists())

    def test_delete_other_user_book_failure(self):
        """
        ログイン状態で他ユーザーの本の削除が失敗することを検証します。
        """
        response = self.client.post(
            reverse("delete-book", kwargs={"pk": self.other_book.pk})
        )
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Book.objects.filter(pk=self.other_book.pk).exists())

    def test_create_review_success(self):
        """
        ログイン状態でレビューの作成が成功することを検証します。
        """
        params = {
            "title": "New Review",
            "text": "New review content",
            "rate": 5,
        }
        response = self.client.post(
            reverse("review", kwargs={"book_id": self.other_book.pk}), params
        )
        self.assertRedirects(
            response, reverse("detail-book", kwargs={"pk": self.other_book.pk})
        )
        self.assertTrue(
            Review.objects.filter(
                title="New Review", text="New review content"
            ).exists()
        )
