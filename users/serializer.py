from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def __str__(self):
        return ""
