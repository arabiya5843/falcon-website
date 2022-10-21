from django.shortcuts import render


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'auth/base.html')
