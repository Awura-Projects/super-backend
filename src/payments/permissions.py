from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if obj.user == user:
            return True

        return False