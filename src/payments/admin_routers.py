from rest_framework import routers

from .admin_viewsets import PaymentViewSet

router = routers.DefaultRouter()
router.register('payment', PaymentViewSet)
