from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):

    class Meta:

        model = Address

        fields = ["city", "state", "zip_code", "district", "number",
                "complement", "created_at", "update_at"]

        read_only_fields = ["created_at", "update_at"]