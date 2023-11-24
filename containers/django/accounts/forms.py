from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    DjangoのデフォルトのUserCreationFormを拡張するカスタムサインアップフォーム。

    Userモデルに基づいて新規ユーザーの作成を可能にするフォームで、
    ユーザー名のみをフィールドに含むシンプルなフォームです。

    Attributes:
    model: django.contrib.auth.models.User
        フォームが作成するモデルのインスタンス。
    fields: tuple
        フォームに表示されるフィールド。このフォームでは 'username' のみを使用。
    """

    class Meta:
        model = User
        fields = ("username",)
