from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    def __str__(self):
        return ""
