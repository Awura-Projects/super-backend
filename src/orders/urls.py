from django.urls import path

from .routers import router
from .views import CartRetrieveAPIView

urlpatterns = [
    path('cart/<int:pk>/', CartRetrieveAPIView.as_view(), name='cart-detail'),
]

urlpatterns += router.urls
