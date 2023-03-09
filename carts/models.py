from django.db import models


class Cart(models.Model):
    cart_total = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    products = models.ManyToManyField(
        "products.Product",
        through="Cart_Product",
        related_name="carts",
    )


class Cart_Product(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ammount = models.IntegerField(default=1)
