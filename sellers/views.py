from .models import Seller
from .serializers import SellerSerializer

from users.permissions import (
    IsSellerAuthorization,
    IsSellerOwnerAuthentication,
    IsSellerListAuthorization,
)

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.exceptions import BadRequest
from rest_framework.views import APIView, Request, Response, status


import ipdb


class RegisterSellerView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerAuthorization]

    serializer_class = SellerSerializer
    queryset = Seller.global_objects.all()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class ListSellerView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerListAuthorization]

    serializer_class = SellerSerializer
    queryset = Seller.global_objects.all()


class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerAuthentication]

    serializer_class = SellerSerializer
    queryset = Seller.global_objects.all()

    lookup_url_kwarg = "seller_id"


class RestoreSellersView(APIView):
    def post(self, req: Request, seller_id: str) -> Response:

        try:

            sellers_obj = Seller.global_objects.get(pk=seller_id)

            if sellers_obj.is_deleted:
                sellers_obj.restore()

                serializer = SellerSerializer(sellers_obj)

                return Response(serializer.data, status=status.HTTP_200_OK)

            raise BadRequest("Undeleted seller")

        except BadRequest as error:

            return Response({"message": error.args}, status=status.HTTP_400_BAD_REQUEST)
