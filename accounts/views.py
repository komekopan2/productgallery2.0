from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class SignupView(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignupForm  # form_classが定義されていないと、model=の中で定義されたモデルに基づいてModelFormが自動作成される
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("index")
    success_message = "サインアップが完了しました。ログインしましょう！"
