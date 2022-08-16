from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter() 
router.register('admin-product', ProductViewSet)

