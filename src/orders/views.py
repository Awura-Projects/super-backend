from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics, views, permissions
from rest_framework.response import Response

from .models import Cart
from .permissions import IsSelfCart
from .serializers import CartSerializer, CartCloseSerializer


class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
        IsSelfCart
    ]

    def get_queryset(self):
        user = self.request.user

        queryset = Cart.objects.filter(user=user)
        return queryset


class CartListAPIView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions
    ]

    def get_queryset(self):
        user = self.request.user

        queryset = Cart.objects.filter(user=user)
        return queryset


class CartCloseAPIView(views.APIView):
    serializer_class = CartCloseSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.DjangoModelPermissions,
    ]

    def get_queryset(self):
        request = self.request
        user = request.user

        return Cart.objects.filter(user=user)

    def post(self, request, format=None):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        cart = serializer.save()
        cart_serializer = CartSerializer(cart, context={'request': request})

        return Response(cart_serializer.data)
