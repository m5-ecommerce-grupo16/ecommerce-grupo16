from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "is_employee",
            "is_superuser",
        ]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(queryset=User.objects.all()),
                ],
                "required": True,
            },
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.set_password(validated_data["password"])

        instance.save()

        return instance
