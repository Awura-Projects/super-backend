from rest_framework import routers

from .viewsets import PaymentViewSet

router = routers.DefaultRouter()
router.register('payment', PaymentViewSet)
