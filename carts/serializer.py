from rest_framework import serializers
from .models import Cart, Cart_Product


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user_id", "cart_total", "products"]
        depth = 1

    def __str__(self):
        return ""


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Product
        fields = ["id", "product", "cart_id", "quantity"]
        depth = 1

    def __str__(self) -> str:
        return ""
