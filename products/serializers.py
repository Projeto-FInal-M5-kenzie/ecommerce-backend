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
                
                Product.objects.bulk_update(product_bulk_update_list, ['stock'])

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

                # Product.objects.bulk_update(
                #     [
                #         product.update()
                #         for product in product_obj_list 
                #     ],
                #     ["stock"],
                # )
                return product_list[0]
            raise Product.DoesNotExist

        except Product.DoesNotExist:

            product_list = [
                Product(
                    **validated_data,
                    category=category_obj,
                    stock=product_qtd,
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

        return dict(quantity=qtd, product=obj.name_product,)

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
        product = validated_data.pop("product")
        user = validated_data.pop("user")
        order_product = OrderProduct.objects.create(**validated_data, product=product)
        order_obj = Order.objects.get_or_create(user=user)[0]
        
        # order_obj.products.add(product)   
        order_obj.order_products.add(order_product)
        # ipdb.set_trace()

        return order_product
        OrderProduct.objects.create(**validated_data, order=order_obj,product=product)
