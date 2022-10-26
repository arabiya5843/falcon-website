from django.urls import path

from orders.views import ProductDetailView, ProductListView
from orders.views.product import FavouriteListView, AddFavouriteView, FavouriteDeleteView

urlpatterns = [
    path('products', ProductListView.as_view(), name='product_list'),
    path('add-favourite/<int:pk>', AddFavouriteView.as_view(), name='add_favourite'),
    path('delete-favourite/<int:pk>', FavouriteDeleteView.as_view(), name='delete_favourite'),
    path('favourite', FavouriteListView.as_view(), name='favourite'),
    path('products/<str:slug>', ProductDetailView.as_view(), name='product_detail')
]


