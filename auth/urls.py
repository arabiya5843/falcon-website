from django.urls import path

from auth.views import *

app_name = 'auth'
urlpatterns = [
    path('login/', login, name='register'),
    path('register/', register, name='register'),
]
