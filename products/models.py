from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=128)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
