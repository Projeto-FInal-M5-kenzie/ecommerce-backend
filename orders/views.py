from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Order
from django.shortcuts import get_object_or_404
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
import ipdb


class OrderView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):

        return Order.objects.filter(user__id=self.request.user.id)

