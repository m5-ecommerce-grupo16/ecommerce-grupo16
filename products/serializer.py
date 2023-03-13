from rest_framework import serializers
from .models import Product
from users.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "user_id",
            "name",
            "price",
            "quantity",
            "description",
            "category",
        ]
        read_only_fields = ["user_id", "user"]


class SummaryProductsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "description", "category"]
        read_only_fields = ["name", "price", "description", "category"]
