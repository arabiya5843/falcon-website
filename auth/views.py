from django.shortcuts import render


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'auth/register.html')


def login(request):
    if request.method == "GET":
        return render(request, 'auth/login.html')
