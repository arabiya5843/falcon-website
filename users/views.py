from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import FormView, TemplateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView

from orders.models import Product, Favourite
from users.forms import AuthLoginForm, CustomUserCreationForm
from users.mixins import AuthUserMixin


class LandingView(TemplateView):
    template_name = 'landing.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


# class ProductListView(ListView):
#     queryset = Product.objects.order_by('-created_at')
#     template_name = ''
#     paginator_class = Paginator

class CustomLoginView(AuthUserMixin, FormView):
    form_class = AuthLoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        # email = form.data.get('email')
        # password = form.data.get('password')
        # user = authenticate(**form.data)
        user = authenticate(**form.data.dict())
        login(self.request, user)
        return super().form_valid(form)


class RegisterView(AuthUserMixin, FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
