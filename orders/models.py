from django.db import models


class Status(models.TextChoices):
    SUCCESS = "Realizado"
    ONGOING = "Em Andamento"
    DELIVERED = "Entregue"


class Order(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.SUCCESS
    )
    date = models.DateTimeField()
    products = models.ManyToManyField(
        "products.Product", through="Order_Product", related_name="orders"
    )


class Order_Product(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()
