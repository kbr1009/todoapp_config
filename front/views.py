from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import DetailView, UpdateView 

from .forms import UserForm

def index(request):
    return render(request, "front/index.html")


@login_required # 追加
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


class UserDetailView(DetailView):
    model = User
    template_name = "front/users/detail.html"


class UserUpdateView(UpdateView):
    model = User
    template_name = 'front/users/update.html'
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('front:users_detai',pk=self.kwargs['pk'])
