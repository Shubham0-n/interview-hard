from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CustomUserForm, UpdateUserForm
from .models import CustomUser

# Create your views here.


class UserListView(ListView):
    model = CustomUser
    template_name = "userlist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CustomUserForm
        return context


class UserCreateView(CreateView):
    model = CustomUser
    template_name = "userlist.html"
    success_url = reverse_lazy("users:user_list")
    form_class = CustomUserForm


class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = "userlist.html"
    success_url = reverse_lazy("users:user_list")
    form_class = UpdateUserForm


class UserDeleteView(DeleteView):
    model = CustomUser
    # template_name="userlist.html"
    success_url = reverse_lazy("users:user_list")
