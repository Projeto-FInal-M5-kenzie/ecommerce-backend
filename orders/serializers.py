from rest_framework import serializers
from .models import Order
from deliveries.serializers import DeliverySerializer


class OrderSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer(required=False)

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
