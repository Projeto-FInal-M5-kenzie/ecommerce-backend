from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdmAuthorization(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        return request.user.is_authenticated and request.user.is_superuser
