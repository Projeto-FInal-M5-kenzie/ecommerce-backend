import datetime
from .models import User
from axes.models import AccessAttempt, AccessFailureLog
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
from .permissions import IsAdmAuthorization, IsUserOwnerAuthentication
import ipdb
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.exceptions import ErrorDetail


class RegisterUserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.global_objects.all()

    def get_queryset(self):

        return self.queryset.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        data = dict(
            message="An email has been sent on your mail.",
        )

        return Response(
            data=data, status=status.HTTP_307_TEMPORARY_REDIRECT, headers=headers
        )


class ActivateUser(APIView):
    def post(self, req: Request, email_token: str) -> Response:
        try:
            # print(req.data)
            users_obj = User.objects.get(email_token=email_token)
            ipdb.set_trace()
            if req.data["is_email_verified"]:
                users_obj.is_email_verified = req.data["is_email_verified"]
                serializer = UserSerializer(users_obj)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            raise ErrorDetail
        except Exception as error:
            return Response(
                data={"Invalid Email token"}, status=status.HTTP_400_BAD_REQUEST
            )

# class LoginView(APIView):
#     def post(self, request: Request) -> Response:
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(
#             request=request,
#             username=serializer.validated_data["username"],
#             password=serializer.validated_data["password"],
#         )

#         if not user:
#             account =  AccessAttempt.objects.get(username=serializer.validated_data["username"])
#             current_time =  datetime.datetime.now()
#             number_of_attempts =  account.failures_since_start
#             threshold = (number_of_attempts / 5)
#             ipdb.set_trace()

#             a = signals.user_login_failed.send(
#                 sender=User,
#                 request=request,
#                 credentials={
#                     'username': serializer.validated_data["username"],
#                 },

#             )
#             return Response(status=403)
#             # return Response(
#             #     {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
#             # )

#         refresh = RefreshToken.for_user(user)

#         token = {"refresh": str(refresh), "access": str(refresh.access_token)}

#         return Response(token)


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
