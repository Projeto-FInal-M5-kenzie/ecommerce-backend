from rest_framework import serializers
from .models import OrderProduct, Product
from orders.models import Order
from addresses.models import Address
from orders.serializers import OrderSerializer
from categories_products.models import Category_product
from django.shortcuts import get_object_or_404

from sellers.serializers import SellerSerializer
from sellers.models import Seller


class ProductSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default=1, write_only=True)
    stock = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data: dict) -> Product:
        product_qtd = 1
        product_qtd = validated_data.pop("quantity")
        category_id = validated_data.pop("category")
        category_obj = Category_product.objects.get(id=category_id)
        seller_obj = validated_data.pop("seller")
        # seller_obj = Seller.objects.filter(id=seller_id).first()

        name_product = validated_data.pop("name_product")

        try:

            product_obj_list = Product.objects.filter(
                name_product=name_product, category=category_obj
            )

            stock = len(product_obj_list)

            if stock > 0:
                product_bulk_update_list = []

                stock += product_qtd

                for product in product_obj_list:
                    product.stock = stock
                    product_bulk_update_list.append(product)

                Product.objects.bulk_update(product_bulk_update_list, ["stock"])

                product_list = [
                    Product(
                        **validated_data,
                        category=category_obj,
                        stock=stock,
                        seller=seller_obj,
                        name_product=name_product
                    )
                    for _ in range(product_qtd)
                ]

                Product.objects.bulk_create(product_list)

                return product_list[0]
            raise Product.DoesNotExist

        except Product.DoesNotExist:

            product_list = [
                Product(
                    **validated_data,
                    category=category_obj,
                    stock=product_qtd,
                    seller=seller_obj,
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

        return dict(
            quantity=qtd,
            product=obj.name_product,
        )

    class Meta:

        model = Product

        fields = [
            "id",
            "name_product",
            "description",
            "price",
            "stock",
            "is_active",
            "created_at",
            "category",
            "quantity",
            "seller",
        ]

        extra_kwargs = {"quantity": {"write_only": True}}
        read_only_fields = ["seller"]


class OrderProductSerializer(serializers.ModelSerializer):
    address = ()

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
        category_obj = Category_product.objects.get(name=validated_data.pop("category"))

        name_product = validated_data.pop("name_product")
        product_qtd = validated_data.pop("quantity_product")
        address = Address.objects.get(id=validated_data.pop("address"))
        user = validated_data.pop("user")

        order_obj = Order.objects.filter(user__id=user.id).first()

        if not order_obj:
            order_obj = Order.objects.create(user=user, address=address)

        count = 0

        products_list = Product.objects.filter(
            name_product=name_product, category=category_obj
        )

        order_product = validated_data

        for product in products_list:
            count += 1
            if count > product_qtd:
                break

            order_product = OrderProduct.objects.get_or_create(
                **validated_data, product=product, quantity_product=product_qtd
            )[0]

            order_obj.order_products.add(order_product)

        return order_product
