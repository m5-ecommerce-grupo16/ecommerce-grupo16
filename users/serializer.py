from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_employee",
            "is_superuser",
            "address",
            "cart"
        ]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(queryset=User.objects.all()),
                ],
                "required": True,
            },
            "password": {"write_only": True},
            "cart": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"] is True:
            return User.objects.create_superuser(**validated_data, is_employee=True)
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(validated_data["password"])
        instance.save()

        return instance
