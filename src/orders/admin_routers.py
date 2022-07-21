from rest_framework import routers

from .admin_viewsets import CartViewSet

router = routers.DefaultRouter()
router.register('cart', CartViewSet)
