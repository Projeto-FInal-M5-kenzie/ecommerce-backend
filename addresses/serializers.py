from rest_framework import serializers

from .models import Address
from sellers.serializers import SellerSerializer
from users.serializers import UserSerializer

import ipdb


class AddressSellerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        seller = validated_data.pop("seller")

        address = Address.objects.get_or_create(**validated_data)[0]

        address.seller = seller

        return address

    seller = SellerSerializer(read_only=True)

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
            "seller",
        ]

        read_only_fields = ["created_at", "update_at"]


class AddressUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data.pop("users")

        address = Address.objects.get_or_create(**validated_data)[0]

        address.users.add(user)

        request = self.context["request"].get_full_path()
        print(request)

        return address

    users = UserSerializer(read_only=True, many=True)

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
            "users",
        ]

        read_only_fields = ["created_at", "update_at"]
