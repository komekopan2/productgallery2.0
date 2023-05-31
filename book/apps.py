from django.apps import AppConfig

# q:このファイルは何？
# a:アプリケーションの設定を行うためのファイル


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'book'
