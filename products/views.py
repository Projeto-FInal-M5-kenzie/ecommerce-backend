from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import OrderProduct, Product
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer, OrderProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status


class ProductView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(**self.request.data)


class ProductCategoryView(APIView):
    def get(self, req: Request, category_id: str) -> Response:

        products_list = Product.objects.filter(category=category_id)

        serializer = ProductSerializer(products_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderProductView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def perform_create(self, serializer):

        product_id = self.kwargs["product_id"]

        product_obj = get_object_or_404(Product, pk=product_id)
        serializer.save(
            user=self.request.user,
            product=product_obj,
            **self.request.data,
        )
