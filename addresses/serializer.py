from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "street",
            "district",
            "city",
            "state",
            "country",
        ]

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
