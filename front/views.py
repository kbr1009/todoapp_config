from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, ListView, DeleteView

from .forms import UserForm, ListForm, CardForm, CardCreateFromHomeForm
from .mixins import OnlyYouMixin
from .models import List, Card

def index(request):
    return render(request, "front/index.html")


class HomeView(LoginRequiredMixin, ListView):
    model = List
    template_name = "front/home.html"
"""
@login_required # 追加
def home(request):
    return render(request, "front/home.html")
"""

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


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'front/users/detail.html'


class UserUpdateView(OnlyYouMixin, UpdateView):
    model = User
    template_name = 'front/users/update.html'
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('front:users_detail', pk=self.kwargs['pk'])


class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "front/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("front:lists_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "front/lists/list.html"

class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = "front/lists/detail.html"

class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "front/lists/update.html"
    form_class = ListForm
    success_url = reverse_lazy("front:home")

    def get_success_url(self):
        return resolve_url('front:lists_detail', pk=self.kwargs['pk'])

class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "front/lists/delete.html"
    form_class = ListForm
    success_url = reverse_lazy("front:home")



class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "front/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("front:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = "front/cards/list.html"


class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = "front/cards/detail.html"


class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = "front/cards/update.html"
    form_class = CardForm
    success_url = reverse_lazy("front:home")

"""
    def get_success_url(self):
        return resolve_url('front:cards_detail', pk=self.kwargs['pk'])
"""

class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = "front/cards/delete.html"
    form_class = CardForm
    success_url = reverse_lazy("front:home")


class CardCreateFromHomeView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "front/cards/create.html" 
    form_class = CardCreateFromHomeForm
    success_url = reverse_lazy("front:home")

    def form_valid(self, form):
        list_pk = self.kwargs['list_pk']
        list_instance = get_object_or_404(List, pk=list_pk)
        form.instance.list = list_instance
        form.instance.user = self.request.user
        return super().form_valid(form)
