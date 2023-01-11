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
            "cpf",
            "phone",
            "is_active",
            "is_superuser",
            "is_seller",
            "is_deleted",
            "created_at",
            "updated_at",
            "deleted_at",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="Email already exists.",
                    )
                ]
            },
            "cpf": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="CPF already exists.",
                    )
                ]
            },
        }
        read_only_fields = ["is_superuser", "is_active"]

    def create(self, validated_data):
        USERS_ADM = (
            "lucas@adm.com",
            "geovane@adm.com",
            "gutemberg@adm.com",
            "guilherme@adm.com",
            "breno@adm.com",
            "joao@adm.com",
        )
        validated_data["is_seller"] = False

        if validated_data["email"] in USERS_ADM:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
