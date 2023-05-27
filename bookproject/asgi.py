"""
ASGI config for bookproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
# q:このファイルは何？
# a:ASGI(Asynchronous Server Gateway Interface)アプリケーション
# q:何をする？
# a:WebサーバーとWebアプリケーションフレームワークの間のインターフェース
# q:どうやって？
# a:django.core.asgi.get_asgi_application()
# q:どうやって使う？
# a:python manage.py runserver

# 多くのリクエストの記録を取って同時に多くの処理ができるようにしている

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookproject.settings')

application = get_asgi_application()
