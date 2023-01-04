from .models import Seller
from .serializers import SellerSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterSellerView(generics.CreateAPIView):
    serializer_class = SellerSerializer


class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsOwnerAuthentication]

    serializer_class = SellerSerializer
    queryset = Seller.objects.all()

    lookup_url_kwarg = "seller_id"
