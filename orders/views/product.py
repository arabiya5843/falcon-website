from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, View

from orders.models import Product, Favourite, Cart


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    slug_url_kwarg = 'slug'


class ProductListView(ListView):
    queryset = Product.objects.order_by('-created_at')
    '''
    select * from products order by created_at desc
    '''
    paginate_by = 1
    model = Product
    template_name = 'product/list.html'

class FavouriteListView(LoginRequiredMixin, ListView):
    template_name = 'product/favourite.html'
    queryset = Favourite.objects.order_by('-created_at')
    context_object_name = 'favourites'


class FavouriteDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        favourite = Favourite.objects.filter(pk=pk).first()
        if favourite:
            favourite.delete()
        return redirect('favourite')


class AddFavouriteView(View):
    def get(self, request, pk, *args, **kwargs):
        favourite, created = Favourite.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            favourite.delete()
        return redirect('product_list')


class CartListView(LoginRequiredMixin, ListView):
    template_name = 'product/cart.html'
    queryset = Cart.objects.order_by('-created_at')
    context_object_name = 'carts'


class CartDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        cart = Cart.objects.filter(pk=pk).first()
        if cart:
            cart.delete()
        return redirect('cart')


class AddCartView(View):
    def get(self, request, pk, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user, product_id=pk)
        if not created:
            cart.delete()
        return redirect('product_list')
