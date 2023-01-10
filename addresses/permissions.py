from rest_framework import permissions
from rest_framework.views import Request, View

from .models import Address


class IsSellerAuthorization(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_authenticated and request.user.is_seller


class IsSellerOwnerAddressAuthentication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Address):
        return (
            request.user.is_authenticated
            and request.user.is_seller
            and request.user == obj.sellers
            and obj.is_deleted == False
        )
