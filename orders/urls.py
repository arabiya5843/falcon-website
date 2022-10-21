from django.urls import path

from orders.views import ProductDetailView, ProductListView

urlpatterns = [
    path('products', ProductListView.as_view(), name='product_list'),
    path('products/<str:slug>', ProductDetailView.as_view(), name='product_detail')
]
