from rest_framework import permissions

class IsDelivery(permissions.BasePermission):
    def has_permission(self, request):
        user = request.user 
        if user.user_type == 'delivery':
            return True
        return False