from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import OrderProduct, Product
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer, OrderProductSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404



class ProductView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(**self.request.data)

    def get_queryset(self):
        route_parameter = self.request.GET.get("product_name")
        if route_parameter:

<<<<<<< HEAD
            return Product.objects.filter(product_name__icontains=route_parameter)

        return super().get_queryset()
=======
class ProductCategoryView(APIView):
    def get(self, req: Request, category_id: str) -> Response:
>>>>>>> 3c378ec (feat: refactoring order product)


<<<<<<< HEAD
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_object(self):

        product_id = self.kwargs["product_id"]
        product_obj = get_object_or_404(Product, pk=product_id)

        return product_obj
=======
        serializer = ProductSerializer(products_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
>>>>>>> 3c378ec (feat: refactoring order product)


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

class OrderProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def get_object(self):

        order_product_id = self.kwargs["order_product_id"]
        order_product_obj = get_object_or_404(OrderProduct, pk=order_product_id)

        return order_product_obj
