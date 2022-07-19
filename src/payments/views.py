from rest_framework import generics, permissions

from .serializers import PaymentSerailzer

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerailzer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
