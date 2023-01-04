from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import OrderProduct
from django.shortcuts import get_object_or_404
from .serializers import OrderProductSerializer


class OrderProductView(generics.ListCreateAPIView):
    
    authentication_classes = [JWTAuthentication]
    
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

    def perform_create(self, serializer):

        product_id = self.kwargs["product_id"]
        
        product_obj = get_object_or_404(OrderProduct, pk=product_id)
        
        serializer.save(clients=self.request.user, product=product_obj,**self.request.data)
        