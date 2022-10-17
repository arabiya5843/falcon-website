from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import *
from django.shortcuts import render

# Create your views here.

# class FirstView(ListView):
#     model = FirstView
#     template_name = "index.html"
def index(request):
    return render(request, 'inbox.html')


def base(request):

    return render(request, "base.html")

def compose(request):

    return render(request, "compose.html")

def confirm_mail(request):

    return render(request, "confirm-mail.html")

def email_detail(request):

    return render(request, "email-detail.html")

def forgot_password(request):

    return render(request, "forgot-password.html")

def inbox(request):

    return render(request, "inbox.html")


def login(request):

    return render(request, "login.html")

def logout(request):

    return render(request, "logout.html")

def profile(request):

    return render(request, "profile.html")

def register(request):

    return render(request, "register.html")

def reset_password(request):

    return render(request, "reset-password.html")

def settings(request):

    return render(request, "settings.html")