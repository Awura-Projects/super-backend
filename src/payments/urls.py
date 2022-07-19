from django.urls import path

from .views import PaymentCreateAPIView, PaymentRetrieveAPIView

urlpatterns = [
    path('payment/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment-detail'),
]
