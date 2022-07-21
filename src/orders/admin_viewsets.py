from rest_framework import viewsets, permissions

from .models import Cart
from .serializers import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        permissions.DjangoModelPermissions,
    ]
