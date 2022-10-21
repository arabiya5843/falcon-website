from django.urls import path

from auth.views import register

app_name = 'auth'
urlpatterns = [
    path('register/', register, name='register')
]
