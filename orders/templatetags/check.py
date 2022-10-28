from django import template

from orders.models import Cart, Favourite

register = template.Library()


@register.filter
def has_cart(product, user):
    return Cart.objects.filter(user=user, product=product).exists()


@register.filter
def has_fav(product, user):
    return Favourite.objects.filter(user=user, product=product).exists()
