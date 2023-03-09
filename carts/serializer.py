from rest_framework import serializers
from .models import Cart, Cart_Product
from products.models import Product


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ["id", "cart_total", "cart_product_set"]
        depth = 2

        read_only_fields = ["cart_product_set"]

    def __str__(self):
        return ""


class CartProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all())

    class Meta:
        model = Cart_Product
        fields = ["id", "cart", "product", "ammount"]
        read_only_fields = ["cart"]

    def create(self, validated_data):
        product = validated_data.pop("product")

        return Cart_Product.objects.create(
            **validated_data, product=product)

    def __str__(self) -> str:
        return ""
