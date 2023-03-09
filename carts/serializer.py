from rest_framework import serializers
from .models import Cart, Cart_Product


class CartSerializer(serializers.ModelSerializer):
    def cart_total(self):
        return sum(item.product.price * item.amount for item in self.cart_product.all())

    class Meta:
        model = Cart
        fields = ["id", "cart_total", "products"]
        depth = 1

    def __str__(self):
        return ""


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Product
        fields = ["id", "cart_id", "product", "ammount"]

    def __str__(self) -> str:
        return ""
