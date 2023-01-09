from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import OrderProduct, Product
from .serializers import ProductSerializer, OrderProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class ProductView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(**self.request.data)

    def get_queryset(self):
        route_parameter = self.request.GET.get("name_product")
        
        if route_parameter:
            return Product.objects.filter(name_product__icontains=route_parameter)

        return super().get_queryset()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):

        product_id = self.kwargs["product_id"]
        product_obj = get_object_or_404(Product, pk=product_id)

        return product_obj


class OrderProductView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def perform_create(self, serializer):

        # product_id = self.kwargs["product_id"]

        # product_obj = get_object_or_404(Product, pk=product_id)
        serializer.save(
            user=self.request.user,
            # product=product_obj,
            **self.request.data,
        )

class OrderProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def get_object(self):

        order_product_id = self.kwargs["order_product_id"]
        order_product_obj = get_object_or_404(OrderProduct, pk=order_product_id)

        return order_product_obj
