from .models import Seller
from .serializers import SellerSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
import ipdb


class RegisterSellerView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = SellerSerializer
    queryset = Seller.objects.all()

    def perform_create(self, serializer):
        # self.request.user.is_superuser = True
        serializer.save(client=self.request.user)


class SellerDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsOwnerAuthentication]

    serializer_class = SellerSerializer
    queryset = Seller.objects.all()

    lookup_url_kwarg = "seller_id"
