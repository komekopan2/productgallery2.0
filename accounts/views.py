from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import login


# The function-based view for user signup
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            messages.success(request, "アカウントは正常に作成されました！")
            # Redirect to the 'index' page after successful signup
            return redirect(reverse("index"))
    else:
        form = SignupForm()

    return render(request, "accounts/signup.html", {"form": form})
