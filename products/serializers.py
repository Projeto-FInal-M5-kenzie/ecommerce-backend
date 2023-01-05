from rest_framework import serializers
from .models import OrderProduct, Product
from categories_products.models import Category_product
import ipdb

class ProductSerializer(serializers.ModelSerializer):
  
    stock = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data: dict) -> Product:
        category_id = validated_data.pop("category")
        # categoid = validated_data.pop("category")
        # dict_a = dict(id=category_id)
        category_obj = Category_product.objects.get(id=category_id)

        name_product = validated_data.pop("name_product")
        
        try:

            stock = len(Product.objects.filter(name_product=name_product, category=category_obj))
            product_obj = Product.objects.filter(name_product=name_product, category=category_obj)

            if len(product_obj) > 0:
             
                stock += 1
               
                return Product.objects.create(
                    **validated_data,
                    category=category_obj,
                    stock=stock,
                    name_product=name_product
                )

            raise Product.DoesNotExist

        except Product.DoesNotExist:
          
            stock += 1
          
            return Product.objects.create(
                **validated_data,
                category=category_obj,
                stock=stock,
                name_product=name_product
            )


    def get_stock(self, obj):

        category_obj = Category_product.objects.get(id=obj.category.id)

        qtd = len(Product.objects.filter(name_product=obj.name_product, category=category_obj))
       
        return dict(
            quantity=qtd, 
            product=obj.name_product
        )


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
        ]


class OrderProductSerializer(serializers.ModelSerializer):
   
    class Meta:

        model = OrderProduct

        fields = [
            "id",
            "quantity_product",
            "subtotal_price",
            "total_price",
            "created_at",
            "updated_at",
            "clients",
            "products",
        ]

    def create(self, validated_data: dict) -> OrderProduct:

        return OrderProduct.objects.create(**validated_data)
