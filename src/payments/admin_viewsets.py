from rest_framework import viewsets, permissions

from .serializers import PaymentSerailzer
from .models import Payment

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerailzer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser,
        permissions.DjangoModelPermissions,
    ]
