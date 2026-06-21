import secrets

from django.views.generic import CreateView
from .models import User
from .forms import UserRegisterForm
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect

from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
