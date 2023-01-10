from rest_framework import serializers
from .models import Order
from addresses.models import Address
import ipdb

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Order

        fields = [
            "id",
            "created_at",
            "updated_at",
            # "user",
            "address",
            "products",
            "order_products"
            # "delivery",
        ]
        depth = 1

    def create(self, validated_data: dict) -> Order:

        return Order.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        if validated_data["address"]:
            address = Address.objects.get(id=validated_data.pop("address"))

        # for key, _ in validated_data.items():
            # ipdb.set_trace()
            instance.address = address
                # setattr(instance, key, address)

            instance.save()

            return instance
