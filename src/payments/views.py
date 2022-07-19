from rest_framework import generics, permissions

from .models import Payment
from .serializers import PaymentSerailzer

class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerailzer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerailzer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request
        queryset = Payment.objects.filter(user=user)

        return queryset
