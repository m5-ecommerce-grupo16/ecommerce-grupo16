from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    def __str__(self):
        return ""
