from django.db.models import (Model, CharField, DecimalField, SlugField, IntegerField, ForeignKey, CASCADE, ImageField,
                              JSONField, TextField, DateTimeField, SmallIntegerField)

from users.models import User


class Base(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=155)
    slug = SlugField(max_length=155, unique=True)

    def __str__(self):
        return f"{self.name}"


class Product(Base):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    description = TextField(null=True, blank=True)
    discount = SmallIntegerField(default=0)
    price = DecimalField(decimal_places=2, max_digits=9)
    category = ForeignKey(Category, CASCADE)
    spec = JSONField(default=dict)

    @property
    def get_price(self):
        if not self.discount:
            return self.price
        return self.price - self.price * self.discount / 100

    def __str__(self):
        return f"{self.name}"


class Favourite(Base):
    product = ForeignKey('orders.Product', CASCADE)
    user = ForeignKey('users.User', CASCADE)


class Cart(Base):
    product = ForeignKey('orders.Product', CASCADE)
    user = ForeignKey('users.User', CASCADE)

