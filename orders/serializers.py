from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:

        model = Order

        fields = [
            "id",
            "created_at",
            "updated_at",
            "user",
            "delivery",
        ]

    def create(self, validated_data: dict) -> Order:

        return Order.objects.create(**validated_data)
