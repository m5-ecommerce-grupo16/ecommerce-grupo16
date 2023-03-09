from rest_framework import permissions
from .models import Product
from rest_framework.views import Request, View


class IsOwnerOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Product) -> bool:
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return obj.user_id == request.user.id


class PermissionAdd(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.user.is_employee is False or request.user.is_superuser is False:
            return False
        return True
