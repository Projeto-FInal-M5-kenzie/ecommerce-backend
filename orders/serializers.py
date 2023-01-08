from rest_framework import serializers
from .models import Order
import ipdb

class OrderSerializer(serializers.ModelSerializer):
    # products = serializers.SerializerMethodField()

    # def get_products(self, obj):
    #     ipdb.set_trace()
    class Meta:

        model = Order

        fields = [
            "id",
            "created_at",
            "updated_at",
            # "user",
            "products",
            "order_products"
            # "delivery",
        ]
        depth = 1

    def create(self, validated_data: dict) -> Order:

        return Order.objects.create(**validated_data)
