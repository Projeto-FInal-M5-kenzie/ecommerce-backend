from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import OrderProduct, Product
from django.shortcuts import get_object_or_404
from .serializers import OrderProductSerializer, ProductSerializer
from categories_products.models import Category_product
import ipdb


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(**self.request.data)


class ProductCategoryView(generics.ListAPIView):
   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):
       
        category_id = self.kwargs["category_id"]
      
        category_obj = get_object_or_404(Category_product, pk=category_id)
        
        products_list = Product.objects.filter(category=category_obj)
       
        return products_list


class OrderProductView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]

    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def perform_create(self, serializer):

        product_id = self.kwargs["product_id"]

        product_obj = get_object_or_404(OrderProduct, pk=product_id)

        serializer.save(
            clients=self.request.user, product=product_obj, **self.request.data
        )
