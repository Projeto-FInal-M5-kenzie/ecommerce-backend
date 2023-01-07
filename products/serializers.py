from rest_framework import serializers
from .models import OrderProduct, Product
from orders.models import Order
from categories_products.models import Category_product
import ipdb


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default=1, write_only=True)
    stock = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data: dict) -> Product:
        product_qtd = 1
        product_qtd = validated_data.pop("quantity")
        category_id = validated_data.pop("category")
        category_obj = Category_product.objects.get(id=category_id)

        name_product = validated_data.pop("name_product")

        try:

            stock = len(
                Product.objects.filter(
                    name_product=name_product,
                    category=category_obj,
                )
            )

            product_obj_list = Product.objects.filter(
                name_product=name_product, category=category_obj
            )

            if len(product_obj_list) > 0:

                stock += product_qtd
                product_list = [
                    Product(
                        **validated_data,
                        category=category_obj,
                        stock=stock,
                        name_product=name_product
                    )
                    for _ in range(product_qtd)
                ]

                Product.objects.bulk_create(product_list)

                return product_list[0]

            raise Product.DoesNotExist

        except Product.DoesNotExist:

            stock += product_qtd

            product_list = [
                Product(
                    **validated_data,
                    category=category_obj,
                    stock=stock,
                    name_product=name_product
                )
                for _ in range(product_qtd)
            ]

            Product.objects.bulk_create(product_list)
            return product_list[0]

    def get_stock(self, obj):

        category_obj = Category_product.objects.get(id=obj.category.id)

        qtd = len(
            Product.objects.filter(
                name_product=obj.name_product,
                category=category_obj,
            )
        )

        return dict(quantity=qtd, product=obj.name_product)

    class Meta:

        model = Product

        fields = [
            "id",
            "name_product",
            "description",
            "is_active",
            "price",
            "stock",
            "created_at",
            "category",
            "quantity",
        ]

        extra_kwargs = {"quantity": {"write_only": True}}


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = OrderProduct

        fields = [
            "id",
            "quantity_product",
            "order",
            "product",
        ]

        depth = 1

    def create(self, validated_data: dict) -> OrderProduct:
        ipdb.set_trace()

        user = validated_data.pop("user")
        order_obj = Order.objects.create(user=user)
        return OrderProduct.objects.create(**validated_data, order=order_obj)
