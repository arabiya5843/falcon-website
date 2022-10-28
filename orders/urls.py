from django.urls import path

from orders.views import ProductDetailView, ProductListView
from orders.views.product import FavouriteListView, CartAddView, AddFavouriteView, CartListView

urlpatterns = [
    path('products', ProductListView.as_view(), name='product_list'),
    path('add-favourite/<int:pk>', AddFavouriteView.as_view(), name='add_favourite'),
    path('favourite', FavouriteListView.as_view(), name='favourite'),
    path('cart', CartListView.as_view(), name='cart'),
    path('add-cart/<int:pk>', CartAddView.as_view(), name='add-cart'),
    path('products/<str:slug>', ProductDetailView.as_view(), name='product_detail')
]


