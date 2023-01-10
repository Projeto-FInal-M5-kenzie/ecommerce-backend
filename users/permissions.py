from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb

from .models import User
from sellers.models import Seller


class IsAdmAuthorization(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsSellerAuthorization(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_seller
            and request.user.is_deleted == False
        )


class IsSellerOwnerAuthentication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Seller):
        return (
            request.user.is_authenticated
            and request.user == obj.client
            and obj.is_deleted == False
        )


class IsUserOwnerAuthentication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User):
        return (
            request.user.is_authenticated
            and request.user.is_superuser
            or request.user == obj
            and obj.is_deleted == False
        )
