from rest_framework import serializers
from .models import Order, Order_Product
from rest_framework.exceptions import ValidationError


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user_id", "status", "date", "products"]
        depth = 1


class Order_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = ["product_id", "order_id"]

    def __str__(self) -> str:
        return ""
