from rest_framework import routers

from .admin_viewsets import (
    EmployeeViewSet, SupplierViewSet,
    DeliveryViewSet, CustomerViewSet,
)

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet)
router.register('supplier', SupplierViewSet)
router.register('delivery', DeliveryViewSet)
router.register('customer', CustomerViewSet)
