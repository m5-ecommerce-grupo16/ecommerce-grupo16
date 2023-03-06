from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    def __str__(self):
        return ""
