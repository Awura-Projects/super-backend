from rest_framework import routers

from .viewsets import (
    EmployeeViewSet, SupplierViewSet,
    DeliveryViewSet
)

urlpatterns = []

router = routers.DefaultRouter()
router.register('employee', EmployeeViewSet)
router.register('supplier', SupplierViewSet)
router.register('delivery', DeliveryViewSet)

urlpatterns += router.urls
