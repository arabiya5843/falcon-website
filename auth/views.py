from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import *


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'auth/register.html')


def login(request):
    if request.method == "GET":
        return render(request, 'auth/login.html')
