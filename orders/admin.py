from django.contrib import admin

from orders.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)