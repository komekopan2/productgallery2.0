from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Book
from django.urls import reverse
from django.test import TestCase, Client


class BookCRUDTest(TestCase):
    def setUp(self):
        # ユーザーセットアップ
        self.username = "testuser"
        self.password = "Pa74107410"
        self.user = User.objects.create_user(
            self.username, "test@example.com", self.password
        )

        # クライアントセットアップ
        self.client = Client()
        self.client.login(username=self.username, password=self.password)

        # Bookインスタンスのセットアップ
        self.book = Book.objects.create(
            title="Test Book", text="Test Content", category="web", user=self.user
        )

    def test_create_book(self):
        # Book作成ビューをテスト
        response = self.client.post(
            reverse("create-book"),
            {
                "title": "New Book",
                "text": "New text content",
                "category": "mobile",
            },
        )

        # リダイレクトされるか確認
        self.assertEqual(response.status_code, 302)

        # データベースに新しいBookが追加されたか確認
        new_book = Book.objects.get(title="New Book")
        self.assertIsNotNone(new_book)

    def test_read_book_detail(self):
        # Book詳細ビューをテスト
        response = self.client.get(reverse("detail-book", kwargs={"pk": self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_update_book(self):
        # Book更新ビューをテスト
        response = self.client.post(
            reverse("update-book", kwargs={"pk": self.book.pk}),
            {
                "title": "Updated Book",
                "text": "Updated text content",
                "category": self.book.category,
            },
        )

        # リダイレクトされるか確認
        self.assertEqual(response.status_code, 302)

        # Bookが更新されたか確認
        updated_book = Book.objects.get(pk=self.book.pk)
        self.assertEqual(updated_book.title, "Updated Book")

    def test_delete_book(self):
        # Book削除ビューをテスト
        response = self.client.post(reverse("delete-book", kwargs={"pk": self.book.pk}))

        # リダイレクトされるか確認
        self.assertEqual(response.status_code, 302)

        # Bookが削除されたか確認
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(pk=self.book.pk)
