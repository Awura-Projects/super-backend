import re
from rest_framework import permissions

class IsEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # has_permission =
        user = request.user
        if user.user_type == 'employee':
            return True
        return False