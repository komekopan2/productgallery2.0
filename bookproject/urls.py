"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# q:このファイルは何？
# a:djangoのURLconf
# q:何をする？
# a:URLとviewを紐付ける
# q:どうやって？
# a:urlpatternsにpathを追加する
# q:どうやって使う？
# a:python manage.py runserver

# ブラウザから受け取ったrequestを基に、views.pyに対して指示を出す
# views.pyはrequestを受け取り、models.pyに対して指示を出す

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("book.urls")),
]

try:
    from . import local_settings

    urlpatterns += static(
        local_settings.STATIC_URL, document_root=local_settings.STATICFILES_DIRS
    )
    urlpatterns += static(
        local_settings.MEDIA_URL, document_root=local_settings.MEDIA_ROOT
    )
except:
    pass
