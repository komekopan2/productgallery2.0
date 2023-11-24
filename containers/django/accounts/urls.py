from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

"""
accountsアプリのURL設定
"""

app_name = "accounts"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", views.signup_view, name="signup"),
]
