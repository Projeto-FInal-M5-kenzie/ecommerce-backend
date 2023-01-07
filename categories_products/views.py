from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from .serializers import CategorySerializer
from products.serializers import ProductSerializer
from .models import Category_product
from rest_framework.views import APIView, Request, Response, status
from django.core.exceptions import BadRequest
from products.models import Product


class CategoryView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    # permission_classes = []

    queryset = Category_product.global_objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]

    queryset = Category_product.global_objects.all()
    serializer_class = CategorySerializer

    def get_object(self):

        category_id = self.kwargs["category_id"]

        category_obj = get_object_or_404(Category_product, pk=category_id)
        products_list = Product.objects.filter(category=category_obj)
        # ipdb.set_trace()
        return category_obj


class RestoreCategoryView(APIView):
    def post(self, req: Request, category_id: str) -> Response:

        try:

            category_obj = Category_product.global_objects.get(pk=category_id)

            if category_obj.is_deleted:
                category_obj.restore()

                serializer = CategorySerializer(category_obj)

                return Response(serializer.data, status=status.HTTP_200_OK)

            raise BadRequest("Undeleted category")

        except BadRequest as error:

            return Response({"message": error.args}, status=status.HTTP_400_BAD_REQUEST)


class ProductCategoryView(APIView):
    def get(self, req: Request, category_id: str) -> Response:

        products_list = Product.objects.filter(category=category_id)

        if len(products_list) == 0:
            return Response(
                {"detail": "No products linked to category"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = ProductSerializer(products_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
