from rest_framework import serializers
from .models import Order, Order_Product
from products.serializer import SummaryProductsSerilizer
from carts.models import Cart_Product
from rest_framework.exceptions import APIException


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["user_id", "id", "status", "date", "products"]
        depth = 1


class ProductSeriallizer_Order(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = ["ammount", "product"]
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
        order = Order.objects.create(**validated_data, user=user)
        cart_products = Cart_Product.objects.filter(cart_id=user.cart.id)

        for cart_product in cart_products:
            Order_Product.objects.create(
                product=cart_product.product, order=order, ammount=cart_product.ammount
            )
            cart_product.product.quantity -= cart_product.ammount

            if cart_product.product.quantity <= cart_product.ammount:
                error = APIException(
                    "Não tem estoque suficiente para o produto"
                    + cart_product.product.name
                )
                error.status_code = 400
                raise error

            cart_product.product.save()
            cart_product.delete()

        return order
