from rest_framework import serializers
from .models import Cart, Cart_Product
from products.models import Product


class ProductSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'description', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    products = ProductSummarySerializer(many=True)

    class Meta:
        model = Cart
        fields = ["id", "cart_total", "products"]

    def __str__(self):
        return ""


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Product
        fields = ["id", "cart_id", "product", "ammount"]

    def __str__(self) -> str:
        return ""
