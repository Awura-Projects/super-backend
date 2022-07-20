from django.urls import path

from .views import PaymentListCreateAPIView, PaymentRetrieveAPIView

urlpatterns = [
    path('payment/', PaymentListCreateAPIView.as_view(), name='payment-create'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment-detail'),
]
