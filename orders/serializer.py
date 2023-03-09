from rest_framework import serializers
from .models import Order, Order_Product


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user", "order_total", "status", "date", "products"]


class Order_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = ["product", "order", "quantity"]

    def __str__(self) -> str:
        return ""
