from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, View

from orders.models import Product, Favourite, Cart


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    slug_url_kwarg = 'slug'


class ProductListView(ListView):
    queryset = Product.objects.order_by('-created_at')
    model = Product
    template_name = 'product/list.html'


class FavouriteListView(LoginRequiredMixin, ListView):
    template_name = 'product/favourite.html'
    queryset = Favourite.objects.order_by('-created_at')
    context_object_name = 'favourites'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class CartListView(LoginRequiredMixin, ListView):
    template_name = 'product/cart.html'
    queryset = Cart.objects.annotate(
        real_price=F('product__price') - F('product__price') * F('product__discount') / 100
    ).order_by('-created_at')
    context_object_name = 'carts'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        # price - price * discount / 100
        summa = sum(Cart.objects.filter(
            user=self.request.user
        ).annotate(
            real_price=F('product__price') - F('product__price') * F('product__discount') / 100
        ).values_list(
            'real_price', flat=True)
        )
        context['total_price'] = summa
        return context


class CartAddView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            cart.delete()
        return redirect(request.GET.get('url', 'product_list'))


class AddFavouriteView(View):
    def get(self, request, pk, *args, **kwargs):
        favourite, created = Favourite.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            favourite.delete()
        return redirect(request.GET.get('url', 'product_list'))
