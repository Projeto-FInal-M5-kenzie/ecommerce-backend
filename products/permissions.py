from rest_framework import permissions
from rest_framework.views import Request, View
import ipdb

from sellers.models import Seller
from products.models import Product


class IsSellerOwnerAuthenticationProduct(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Seller):
        return (
            request.user.is_authenticated
            and request.user.is_seller
            and request.user == obj.client
            and obj.is_deleted == False
        )
