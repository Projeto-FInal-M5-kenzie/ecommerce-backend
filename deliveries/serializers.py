from rest_framework import serializers

from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery

        fields = ["id", "delivery", "created_at", "updated_at", "addresses"]

        read_only_fields = ["addresses"]
