from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Address

class AddressSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Address:

        return Address.objects.create(**validated_data)

    
    def update(self, instance: Address, validated_data: dict) -> Address:
        
        for key, value in validated_data.items():
              
            setattr(instance, key, value)
       
        instance.save()
       
        return instance

    
class Meta:

        model = Address
        fields = [
            "id", "city", "state", "zip_code", "district", "updated_at", "number", "complement", "update_at"
        ]
        