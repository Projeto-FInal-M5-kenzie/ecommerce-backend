from rest_framework import serializers

from .models import Cart

from users.serializers import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    client = UserSerializer()

    class Meta:
        model = Cart

        fields = [
            "id",
            "subtotal_price",
            "frete",
            "total_price",
            "client",
            "delivery",
            "payment",
            "product",
        ]

        read_only_fields = ["client"]
