from rest_framework import generics, permissions

from .models import Payment
from .permissions import IsOwner
from .serializers import PaymentSerailzer

class PaymentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PaymentSerailzer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request.user
        queryset = Payment.objects.filter(user=user)

        return queryset

class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerailzer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwner,
    ]

    def get_queryset(self):
        user = self.request.user
        queryset = Payment.objects.filter(user=user)

        return queryset
