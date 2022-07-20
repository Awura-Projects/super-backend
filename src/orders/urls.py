from django.urls import path

from .routers import router
from .views import CartRetrieveDestroyAPIView, CartCloseAPIView, CartListAPIView

urlpatterns = [
    path('cart/<int:pk>/', CartRetrieveDestroyAPIView.as_view(), name='cart-detail'),
    path('cart/', CartListAPIView.as_view(), name='cart-list'),
    path('cart/close/', CartCloseAPIView.as_view(), name='cart-close'),
]

urlpatterns += router.urls
