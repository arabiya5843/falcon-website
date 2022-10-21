from django.views.generic import DetailView, ListView

from orders.models import Product


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    slug_url_kwarg = 'slug'


class ProductListView(ListView):
    queryset = Product.objects.order_by('-created_at')
    '''
    select * from products order by created_at desc
    '''
    model = Product
    template_name = 'product/list.html'
