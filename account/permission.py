from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated, PermissionDenied


class IsAuthenticatedAndOwnerUser(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        raise NotAuthenticated("you have to login.")

    def has_object_permission(self, request, view, obj):
        print(request.user.email , obj.email)
        if request.user.email == obj.email:
            return True

        raise PermissionDenied("you don't have access to this page!!!")
