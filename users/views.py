from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404

from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmAuthorization


class RegisterUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsOwnerAuthentication]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    lookup_url_kwarg = "user_id"


class UserAccessSellerView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmAuthorization]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs["user_id"])

    lookup_url_kwarg = "user_id"
