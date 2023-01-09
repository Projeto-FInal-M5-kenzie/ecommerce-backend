from rest_framework import serializers
from .models import Address
import ipdb


class AddressSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.pop("users")

        address = Address.objects.get_or_create(**validated_data)[0]

        address.users.add(user)

        return address

    def create(self, validated_data):
        user = validated_data.pop("users")
        seller = validated_data.pop("sellers")

        address = Address.objects.get_or_create(**validated_data)[0]

        if user:
            address.users.add(user)
        elif seller:
            address.sellers.add(seller)

        return address
    
    class Meta:

        model = Address

        fields = [
            "id",
            "city",
            "state",
            "zip_code",
            "district",
            "number",
            "complement",
            "created_at",
            "update_at",
        ]

        read_only_fields = ["created_at", "update_at"]
