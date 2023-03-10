from rest_framework import serializers
from .models import Order, Order_Product
from products.serializer import SummaryProductsSerilizer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user_id", "id", "status", "date", "products"]
        depth = 1


class ProductSeriallizer_Order(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = ["ammount", "product"]
        read_only_fields = ["ammount", "product"]
        depth = 1

    product = SummaryProductsSerilizer(read_only=True)


class Order_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "order", "summary"]
        read_only_fields = ["id", "order", "summary"]

    order = OrderSerializer(read_only=True)
    summary = ProductSeriallizer_Order(read_only=True, many=True)

    def create(self, validated_data):
        user = validated_data.pop("user")
        products = user.cart.products
        order = Order.objects.create(**validated_data, user=user)

        order.products.set(products.all())
        return order
