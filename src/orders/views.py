from rest_framework import generics

from .models import Cart
from .permissions import IsSelfCart
from .serializers import CartSerializer

class CartRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsSelfCart]

    def get_queryset(self):
        user = self.request.user

        queryset = Cart.objects.filter(user=user)
        return queryset
