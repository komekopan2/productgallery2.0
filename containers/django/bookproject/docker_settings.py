from .settings import *

# DEBUGを.envから取得
# envファイルにTrue、Falseと書くとDjangoがString型と認識してしまいます
# os.environ.get("DEBUG") == "True"を満たすとboolean型のTrueになり、
# env内のDEBUGがTrue以外ならFalseになります
DEBUG = os.environ.get("DEBUG") == "True"

# ALLOWED_HOSTSを.envから取得
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

SECRET_KEY = os.environ.get("SECRET_KEY")

if DEBUG:
    # STATICFILES_DIRSは開発環境でのみ使用し、本番環境ではSTATIC_ROOTを使用します。
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:
    # STATIC_ROOTを設定
    STATIC_ROOT = "/static/"
    MEDIA_ROOT = "/media/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "bookproject",
        # 'USER': 'postgres',
        # 'PASSWORD': 'Pr794613',
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "db",
        "PORT": 5432,
        # "OPTIONS": {
        #     "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        # },
    }
}
