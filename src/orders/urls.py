from django.urls import path

from .routers import router
from .views import CartRetrieveAPIView, CartCloseAPIView

urlpatterns = [
    path('cart/<int:pk>/', CartRetrieveAPIView.as_view(), name='cart-detail'),
    path('cart/', CartCloseAPIView.as_view(), name='cart-close'),
]

urlpatterns += router.urls
