from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Book, Review
from ..forms import BookForm, ReviewForm
from ..consts import MAX_RATE


class BookReviewTest(TestCase):
    def setUp(self):
        # テストユーザーを作成します。
        self.user_password = "Pa74107410"
        self.user = User.objects.create_user(
            "testuser", "test@example.com", self.user_password
        )

        # Bookのサンプルデータを作成します。
        self.book = Book.objects.create(
            title="Sample Book",
            text="Sample text content",
            category="web",
            user=self.user,
        )

        # Reviewのサンプルデータを作成します。
        self.review = Review.objects.create(
            book=self.book,
            title="Sample Review",
            text="This is a sample review",
            rate=5,
            user=self.user,
        )

    def test_book_creation(self):
        # Bookインスタンスが正しく作成されたかをテストします。
        self.assertEqual(self.book.title, "Sample Book")
        self.assertEqual(self.book.user, self.user)

    def test_review_creation(self):
        # Reviewインスタンスが正しく作成されたかをテストします。
        self.assertEqual(self.review.book, self.book)
        self.assertEqual(self.review.rate, 5)
        self.assertEqual(self.review.user, self.user)

    def test_book_form(self):
        # BookFormが正しくバリデーションを行い、データを保存するかをテストします。
        form_data = {"title": "Another Book", "text": "Some text", "category": "mobile"}
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Formを保存し、インスタンスを取得します。
        book_instance = form.save(commit=False)
        book_instance.user = self.user  # BookFormには'user'フィールドがないため、手動で追加します。
        book_instance.save()

        # Bookインスタンスが正しく保存されたかをテストします。
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest("id").title, "Another Book")

    def test_review_form(self):
        # ReviewFormが正しくバリデーションを行い、データを保存するかをテストします。
        form_data = {"title": "Great Book!", "text": "Loved it", "rate": MAX_RATE}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Formを保存し、インスタンスを取得します。
        review_instance = form.save(commit=False)
        review_instance.book = self.book
        review_instance.user = self.user
        review_instance.save()

        # Reviewインスタンスが正しく保存されたかをテストします。
        self.assertEqual(Review.objects.count(), 2)
        self.assertEqual(Review.objects.latest("id").title, "Great Book!")
