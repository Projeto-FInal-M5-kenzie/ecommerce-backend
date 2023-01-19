from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.core.exceptions import BadRequest
from django.contrib.auth import authenticate, signals
from .models import User
from .serializers import UserSerializer
from .permissions import (
    IsAdmAuthorization,
    IsUserOwnerAuthentication,
    IsListUserAuthorizationAdm,
)
from .utils import send_otp_mail
import random
import ipdb


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response(
                {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
            )

        user_obj = User.objects.get(username=user.username)
        otp = random.randint(1000, 9999)
        user_obj.otp = otp

        user_obj.save()

        send_otp_mail(email=user_obj.email, otp=otp)
        return Response(
            {"Use PIN sender mail for confirmation your access!"},
            status=status.HTTP_307_TEMPORARY_REDIRECT,
        )


class RegisterUserView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsListUserAuthorizationAdm]

    serializer_class = UserSerializer
    queryset = User.global_objects.all()

    def perform_create(self, serializer):
        serializer.save(is_active=False)
        data = {
            "message": "User created successfully. An email has been sent for your confirmation.",
        }
        return Response(data=data, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return self.perform_create(serializer)


class ListUserView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsListUserAuthorizationAdm]

    serializer_class = UserSerializer
    queryset = User.global_objects.all()

    def get_queryset(self):

        return self.queryset.all()


class ActivateUser(generics.UpdateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsListUserAuthorizationAdm]

    serializer_class = UserSerializer
    queryset = User.global_objects.all()

    def get_object(self):
        email_token = self.kwargs["email_token"]
        return get_object_or_404(User, email_token=email_token)

    def perform_update(self, serializer):
        email_token = self.kwargs["email_token"]
        user = get_object_or_404(User, email_token=email_token)
        serializer.save(is_active=True)
        data = {"message": "User activated successfully.", "user": user.id}
        return Response(data=data, status=status.HTTP_200_OK)

class AccessLoginView(APIView):
    def post(
        self,
        req: Request,
    ) -> Response:
        try:
            if not req.data["pin"]:
                raise KeyError("Invalid PIN")

            users_obj = get_object_or_404(User,otp=req.data["pin"])

            UserSerializer(users_obj)

            message = dict(message="Your access is valid!")

            refresh = RefreshToken.for_user(users_obj)

            token = {
                "message": "Your access is valid!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            return Response(data=token, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            message = dict(message="Invalid PIN")

            return Response(data=message, status=status.HTTP_400_BAD_REQUEST)


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

                serializer = UserSerializer(data=users_obj)

                return Response(serializer.data, status=status.HTTP_200_OK)

            raise BadRequest("Undeleted user")

        except BadRequest as error:

            return Response({"message": error.args}, status=status.HTTP_400_BAD_REQUEST)
