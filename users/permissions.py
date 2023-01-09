from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb


class IsAdmAuthorization(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsSellerAuthorization(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_seller