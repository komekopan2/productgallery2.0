from .common_test import BookExistTestCase
from ..models import Book, Review
from ..forms import BookForm, ReviewForm


class LoginForms(BookExistTestCase):
    """
    ログイン状態のBookFormとReviewFormのテストケース。
    """

    def test_book_form(self):
        """
        BookFormが正しくバリデーションを行い、データを保存するかをテストします。
        """
        form_data = {"title": "Another Book", "text": "Some text", "category": "mobile"}
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

        book_instance = form.save(commit=False)
        book_instance.user = self.my_user
        book_instance.save()

        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.latest("id").title, "Another Book")

    def test_review_form(self):
        """
        ReviewFormが正しくバリデーションを行い、データを保存するかをテストします。
        """
        form_data = {"title": "Great Book!", "text": "Loved it", "rate": 5}
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

        review_instance = form.save(commit=False)
        review_instance.book = self.my_book
        review_instance.user = self.my_user
        review_instance.save()

        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.latest("id").title, "Great Book!")

    def test_book_form_invalid(self):
        """
        BookFormが不正なデータを受け付けないかをテストします。
        """
        form_data = {"title": "", "text": "Some text", "category": "mobile"}
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_review_form_invalid(self):
        """
        ReviewFormが不正なデータを受け付けないかをテストします。
        """
        form_data = {"title": "", "text": "Loved it", "rate": 5}
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
