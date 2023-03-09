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
            "category"
        ]
        read_only_fields = ["user_id", "user"]

    def __str__(self):
        return ""
