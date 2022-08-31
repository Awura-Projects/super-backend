from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, mixins

from .models import Employee, Supplier, Delivery
from .serializers import (
    EmployeeSerializer, EmployeeUpdateSerializer,
    SupplierSerializer, SupplierUpdateSerializer,
    DeliverySerializer, DeliveryUpdateSerializer,
)
from authentication.serializers import UserSerializer


User = get_user_model()


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Employee model serializer
    """
    queryset = Employee.objects.all()
    permission_classes = [permissions.IsAdminUser,
                          permissions.DjangoModelPermissions]
    serializer_class = EmployeeSerializer

    def get_serializer_class(self):
        """
        Override the get_serializer_class method to change serializer on update
        """
        if self.action == 'update':
            return EmployeeUpdateSerializer

        return self.serializer_class


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Supplier model serializer
    """
    queryset = Supplier.objects.all()
    permission_classes = [permissions.IsAdminUser,
                          permissions.DjangoModelPermissions]
    serializer_class = SupplierSerializer

    def get_serializer_class(self):
        """
        Override the get_serializer_class method to change serializer on update
        """
        if self.action == 'update':
            return SupplierUpdateSerializer

        return self.serializer_class


class DeliveryViewSet(viewsets.ModelViewSet):
    """
    Delivery model serializer
    """
    queryset = Delivery.objects.all()
    permission_classes = [permissions.IsAdminUser,
                          permissions.DjangoModelPermissions]
    serializer_class = DeliverySerializer

    def get_serializer_class(self):
        """
        Override the get_serializer_class method to change serializer on update
        """
        if self.action == 'update':
            return DeliveryUpdateSerializer

        return self.serializer_class


class CustomerViewSet(
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    queryset = User.objects.filter(groups__name__in=['customer'])
    permission_classes = [permissions.IsAdminUser,
                          permissions.DjangoModelPermissions]
    serializer_class = UserSerializer
