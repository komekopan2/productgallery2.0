from django.test import TestCase, Client
from django.contrib.auth.models import User
from ..models import Book


class LoginTestCase(TestCase):
    """
    ログイン状態のテストケースの基底クラス。
    """

    def setUp(self):
        self.username = "testuser"
        self.password = "Pa74107410"
        self.my_user = User.objects.create_user(
            username=self.username, password=self.password
        )
        self.client = Client()
        self.client.login(username=self.username, password=self.password)


class BookExistTestCase(LoginTestCase):
    """
    本が存在する状態のテストケースの基底クラス。
    """

    def setUp(self):
        super().setUp()
        self.my_book = Book.objects.create(
            title="Test Book",
            text="Test Content",
            category="web",
            thumbnail="image.png",
            user=self.my_user,
        )

        self.other_user = User.objects.create_user(
            username="otheruser", password="Pa74107410"
        )
        self.other_book = Book.objects.create(
            title="Test Book",
            text="Test Content",
            category="web",
            user=self.other_user,
        )
