from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Category_product
from products.serializers import ProductSerializer
import ipdb

# from django_softdelete.models import


class CategorySerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Category_product:

        return Category_product.objects.create(**validated_data)

    def update(
        self, instance: Category_product, validated_data: dict
    ) -> Category_product:

        for key, value in validated_data.items():

            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:

        model = Category_product
        fields = [
            "id",
            "name",
            "description",
            "is_active",
            "created_at",
            "updated_at",
            "deleted_at",
            "is_deleted",
            "products",
        ]

        read_only_fields = ["products"]

        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Category_product.objects.all(),
                        message="Category already exists.",
                    )
                ]
            },
        }
