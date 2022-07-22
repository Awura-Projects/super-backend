from rest_framework import viewsets, permissions

from .models import Employee, Supplier, Delivery
from .serializers import (
    EmployeeSerializer, EmployeeUpdateSerializer,
    SupplierSerializer, SupplierUpdateSerializer,
    DeliverySerializer, DeliveryUpdateSerializer,
)
from .permissions import (
    IsAdminOrSelfEmployee,
    IsAdminOrSelfSupplier,
    IsAdminOrSelfDelivery,
    IsCustomer
)

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Employee model serializer
    """
    queryset = Employee.objects_with_deleted.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = EmployeeSerializer

    def get_serializer_class(self):
        """
        Override the get_serializer_class method to change serializer on update
        """
        if self.action == 'update':
            return EmployeeUpdateSerializer

        return self.serializer_class

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAdminOrSelfEmployee]
            return [permission() for permission in permission_classes]
        return super().get_permissions()

class SupplierViewSet(viewsets.ModelViewSet):
    """
    Supplier model serializer
    """
    queryset = Supplier.objects_with_deleted.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = SupplierSerializer

    def get_serializer_class(self):
        """
        Override the get_serializer_class method to change serializer on update
        """
        if self.action == 'update':
            return SupplierUpdateSerializer

        return self.serializer_class

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [IsAdminOrSelfSupplier]
            return [permission() for permission in permission_classes]
        return super().get_permissions()

class DeliveryViewSet(viewsets.ModelViewSet):
    """
    Delivery model serializer
    """
    queryset = Delivery.objects_with_deleted.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = DeliverySerializer

    def get_serializer_class(self):
        """
        Override the get_serializer_class method to change serializer on update
        """
        if self.action == 'update':
            return DeliveryUpdateSerializer

        return self.serializer_class

    def get_permissions(self):
        if self.action == 'retrieve':
            permission_classes = [
                IsAdminOrSelfDelivery,
                IsCustomer,
            ]
            return [permission() for permission in permission_classes]
        return super().get_permissions()
