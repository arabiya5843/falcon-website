from django.urls import path
from .views import *

urlpatterns = [
    path('', FirstView.as_view(), name='index'),

    path('base/', base, name='base'),
    path('compose/', compose, name='compose'),
    path('confirm-mail/', confirm_mail, name='confirm-mail'),
    path('email-detail/', email_detail, name='email-detail'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('inbox/', inbox, name='inbox'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register/'),
    path('reset_password/', reset_password, name='reset_password'),
    path('settings/', settings, name='settings'),
]
