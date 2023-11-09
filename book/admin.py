from django.contrib import admin
from .models import Book, Review

# 　管理サイトにBookとReviewを登録

admin.site.register(Book)
admin.site.register(Review)
