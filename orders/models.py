from django.db.models import (Model, CharField, DecimalField, SlugField, IntegerField, ForeignKey, CASCADE, ImageField,
                              JSONField, TextField, DateTimeField, SmallIntegerField)
from django.utils.text import slugify

from users.models import User


class Base(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=155)
    slug = SlugField(max_length=155, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


class Product(Base):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    description = TextField(null=True, blank=True)
    discount = SmallIntegerField(default=0)
    image = ImageField(upload_to='products/')
    price = DecimalField(decimal_places=2, max_digits=9)
    category = ForeignKey(Category, CASCADE)
    spec = JSONField(default=dict)

    def __str__(self):
        return f'{self.name}'

    @property
    def get_price(self):
        if not self.discount:
            return self.price
        return self.price - self.price * self.discount / 100


class Favourite(Base):
    product = ForeignKey('orders.Product', CASCADE)
    user = ForeignKey('users.User', CASCADE)

    def __str__(self):
        return f'{self.user.email}({self.user.id}) -> {self.product.name}'


class Cart(Base):
    product = ForeignKey('orders.Product', CASCADE)
    user = ForeignKey('users.User', CASCADE)
    quantity = SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.id} - {self.product.name} ({self.quantity})'
