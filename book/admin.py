from django.contrib import admin
from .models import Book, Review
# from .models import SampleModel

# Register your models here.
# admin.site.register(SampleModel)

# q:このファイルは何？
# a:管理画面で表示するモデルを登録するためのファイル
# q:管理画面で表示するモデルを登録するためには、どのように記述する？
# a:admin.site.register(モデル名)

admin.site.register(Book)
admin.site.register(Review)
