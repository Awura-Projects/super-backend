from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, views, permissions
from rest_framework.response import Response

from .models import Cart
from .permissions import IsSelfCart
from .serializers import CartSerializer

class CartRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsSelfCart
    ]

    def get_queryset(self):
        user = self.request.user

        queryset = Cart.objects.filter(user=user)
        return queryset

class CartCloseAPIView(views.APIView):
    permission_classes = [
        permissions.IsAuthenticated,
        IsSelfCart
    ]

    def post(self, request, format=None):
        cart_id = request.data.get('cart')
        cart = get_object_or_404(Cart, pk=cart_id)

        cart.closed = True
        cart.closed_time = timezone.now()
        cart.save()
        serializer = CartSerializer(cart)

        return Response(serializer)
