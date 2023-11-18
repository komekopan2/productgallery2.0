from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login


def signup_view(request):
    """
    サインアップ（新規ユーザー登録）ページのビュー関数。

    POSTリクエストで受け取ったユーザー情報を検証し、有効であれば新しいユーザーアカウントを作成し、
    ユーザーをログイン状態にします。ユーザー作成が成功すると、'index'と名付けられたURLにリダイレクトされます。
    GETリクエストの場合は、空のサインアップフォームをユーザーに提示します。

    Parameters:
    request: HttpRequestオブジェクト
        ユーザーからのリクエスト情報を含むオブジェクト。

    Returns:
    HttpResponseオブジェクト
        サインアップフォームをレンダリングしたHTTPレスポンス、またはリダイレクトレスポンス。
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "アカウントは正常に作成されました！")
            return redirect(reverse("index"))
    else:
        form = SignupForm()

    return render(request, "registration/signup.html", {"form": form})
