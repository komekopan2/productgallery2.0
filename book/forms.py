from django import forms
from .models import Book, Review


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "text", "category", "thumbnail", "url"]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "text", "rate"]
