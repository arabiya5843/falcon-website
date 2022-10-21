from django.db.models import (Model, CharField, DecimalField, SlugField, IntegerField, ForeignKey, CASCADE, ImageField,
                              JSONField, TextField, DateTimeField)


class Base(Model):
    updated_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=155)
    slug = SlugField(max_length=155, unique=True)


class Product(Base):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    description = TextField(null=True, blank=True)
    price = DecimalField(decimal_places=2, max_digits=9)
    category = ForeignKey(Category, CASCADE)
    spec = JSONField(default=dict)
