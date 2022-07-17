from rest_framework import permissions

class IsSelfCartItem(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        cart = obj.cart

        if cart.user == user:
            return True

        return False

class IsSelfCart(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if obj.user == user:
            return True

        return False
