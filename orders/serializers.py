from rest_framework import serializers
from .models import Order
from addresses.models import Address

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Order

        fields = [
            "id",
            "created_at",
            "updated_at",
            "address",
            "products",
            "order_products"
        ]
        depth = 1

    def create(self, validated_data: dict) -> Order:

        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if validated_data["address"]:
            address = Address.objects.get(id=validated_data.pop("address"))

            instance.address = address

            instance.save()

            return instance
