from .models import User
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404
from django.core.exceptions import BadRequest

from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmAuthorization, IsUserOwnerAuthentication


class RegisterUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.global_objects.all()

    def get_queryset(self):

        return self.queryset.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwnerAuthentication]

    serializer_class = UserSerializer
    queryset = User.global_objects.all()

    lookup_url_kwarg = "user_id"


class UserAccessSellerView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmAuthorization]

    serializer_class = UserSerializer
    queryset = User.global_objects.all()

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs["user_id"])

    lookup_url_kwarg = "user_id"


class RestoreUsersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmAuthorization]

    def post(self, req: Request, user_id: str) -> Response:

        try:

            users_obj = User.global_objects.get(pk=user_id)

            if users_obj.is_deleted:
                users_obj.restore()

                serializer = UserSerializer(users_obj)

                return Response(serializer.data, status=status.HTTP_200_OK)

            raise BadRequest("Undeleted user")

        except BadRequest as error:

            return Response({"message": error.args}, status=status.HTTP_400_BAD_REQUEST)
