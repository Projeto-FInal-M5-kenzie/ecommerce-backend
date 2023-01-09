from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb

from sellers.models import Seller


class IsAdmAuthorization(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsSellerAuthorization(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_seller


class IsOwnerAuthentication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Seller):
        return request.user.is_authenticated and request.user == obj.client
