from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Seller
from users.serializers import UserSerializer


class SellerSerializer(serializers.ModelSerializer):
    # client = UserSerializer(read_only=True)

    class Meta:
        model = Seller
        fields = [
            "id",
            "username",
            "email",
            "password",
            "company_name",
            "cnpj",
            "is_active",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "company_name": {
                "validators": [
                    UniqueValidator(
                        queryset=Seller.objects.all(),
                        message="Company_name already exists.",
                    )
                ]
            },
            "cnpj": {
                "validators": [
                    UniqueValidator(
                        queryset=Seller.objects.all(),
                        message="CNPJ already exists.",
                    )
                ]
            },
        }

    def create(self, validated_data) -> Seller:
        return Seller.objects.create_superuser(**validated_data)

    def update(self, instance: Seller, validated_data) -> Seller:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
