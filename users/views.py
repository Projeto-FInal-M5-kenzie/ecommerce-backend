from .models import User
from .serializers import UserSerializer

from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsOwnerAuthentication]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "user_id"
