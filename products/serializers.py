from rest_framework import serializers
from .models import OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrderProduct

        fields = [
            "id", "quantity_product", "subtotal_price", "total_price", "created_at", "updated_at", "clients", "products"
        ]


    def create(self, validated_data: dict) -> OrderProduct:
        
        return OrderProduct.objects.create(**validated_data)