from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import OrderProduct, Product
from .serializers import ProductSerializer, OrderProductSerializer

from .permissions import IsSellerOwnerAuthenticationProduct

from addresses.models import Address
from categories_products.models import Category_product
from sellers.models import Seller


class RegisterProductView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerAuthenticationProduct]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):

        seller_id = self.kwargs["seller_id"]
        seller_obj = get_object_or_404(Seller, pk=seller_id)

        self.check_object_permissions(self.request, seller_obj)
        
        serializer.save(**self.request.data, seller=seller_obj)

    lookup_url_kwarg = "seller_id"


class ProductView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
        get_object_or_404(Address, id=self.request.data["address"])

        get_object_or_404(Category_product, name=self.request.data["category"])

        serializer.save(
            user=self.request.user,
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
