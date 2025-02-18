from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated, PermissionDenied


class IsAuthenticatedAndOwner(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        raise NotAuthenticated("You must log in.")

    def has_object_permission(self, request, view, obj):
        if request.user == obj.email:
            return True

        raise PermissionDenied("you don't have access to this page!!!")
