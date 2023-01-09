from rest_framework.generics import ListCreateAPIView
from .models import Address
from .serializers import AddressSellerSerializer, AddressUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from users.models import User
from sellers.models import Seller
from .permissions import IsSellerAuthorization, IsSellerOwnerAddressAuthentication

# Create your views here.


class AddressViewUser(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AddressUserSerializer

    def perform_create(self, serializer):
        return serializer.save(users=self.request.user)

    def get_queryset(self):
        return Address.objects.filter(users__id=self.request.user.id)


class AddressViewSeller(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOwnerAddressAuthentication]

    queryset = Address.objects.filter()
    serializer_class = AddressSellerSerializer

    def perform_create(self, serializer):

        seller_id = self.kwargs["seller_id"]

        seller_obj = get_object_or_404(Seller, pk=seller_id)

        return serializer.save(seller=seller_obj)

    def get_queryset(self):
        seller_id = self.kwargs["seller_id"]

        seller = get_object_or_404(Seller, pk=seller_id)

        return Address.objects.filter(seller_id=seller.id)
