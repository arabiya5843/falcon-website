# Generated by Django 4.1.2 on 2022-10-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(default=1),
        ),
    ]