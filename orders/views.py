from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from addresses.models import Address
from django.shortcuts import get_object_or_404


class OrderView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):

        return Order.objects.filter(user__id=self.request.user.id)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_object(self):

        order_id = self.kwargs["order_id"]

        order_obj = get_object_or_404(Order, pk=order_id)

        return order_obj

    def perform_update(self, serializer):
        
        get_object_or_404(Address, id=self.request.data["address"])

        serializer.save(
            **self.request.data,
        )
