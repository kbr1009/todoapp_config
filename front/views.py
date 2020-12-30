from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, "front/index.html")


def home(request):
    return render(request, "front/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("front:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'front/signup.html', context)
