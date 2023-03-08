# Generated by Django 4.0.7 on 2023-03-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('carts', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(null=True, related_name='carts', through='carts.Cart_Product', to='products.product'),
        ),
    ]