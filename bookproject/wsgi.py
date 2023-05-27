"""
WSGI config for bookproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
# q:このファイルは何？
# a:WSGI(Web Server Gateway Interface)アプリケーション
# q:何をする？
# a:WebサーバーとWebアプリケーションフレームワークの間のインターフェース、翻訳機
# q:どうやって？
# a:django.core.wsgi.get_wsgi_application()
# q:どうやって使う？
# a:python manage.py runserver

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookproject.settings')

application = get_wsgi_application()
