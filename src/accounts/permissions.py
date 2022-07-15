from rest_framework import permissions

class IsAdminOrSelfEmployee(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request
        if not user.is_authenticated:
            return False

        if user.is_staff:
            return True

        employee = user.employee

        if employee == obj:
            return True

        return False

class IsAdminOrSelfSupplier(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request
        if not user.is_authenticated:
            return False

        if user.is_staff:
            return True

        supplier = user.supplier

        if supplier == obj:
            return True

        return False

class IsAdminOrSelfDelivery(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request
        if not user.is_authenticated:
            return False

        if user.is_staff:
            return True

        delivery = user.delivery

        if delivery == obj:
            return True

        return False

class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user.user_type == "customer":
            return True

        return False