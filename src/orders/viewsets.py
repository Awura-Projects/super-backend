from rest_framework import viewsets, mixins, permissions

from .models import CartItem
from .permissions import IsSelfCartItem
from .serializers import CartItemSerializer

class CartItemViewSet(mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = CartItem.objects.all()

    def get_permissions(self):
        action = self.action

        if action == 'update' or action == 'destroy' or action == 'retrieve':
            permission_classes = [
                permissions.IsAuthenticated,
                IsSelfCartItem
            ]
            return [permission() for permission in permission_classes]

        return super().get_permissions()

    def perform_destroy(self, instance):
        product = instance.product
        product.amount += instance.quantity
        product.save()

        instance.delete()
