from rest_framework import routers

from .viewsets import CartItemViewSet

router = routers.DefaultRouter()
router.register('cart-item', CartItemViewSet)
