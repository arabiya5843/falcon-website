from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from users.views import CustomLoginView, RegisterView, DashboardView, LandingView

urlpatterns = [
    path('', LandingView.as_view(), name='landing_page'),
    path('dashboard', DashboardView.as_view(), name='index_page'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('landing_page')), name='logout'),
    path('forgot-password', RegisterView.as_view(), name='forgot_password'),
    path('register', RegisterView.as_view(), name='register'),
]
