from django.urls import path, include

from .views import CustomerSignupAPIView, CustomerUpdateAPIView

urlpatterns = [
    path('', include("accounts.routers")),
    path('customer/signup/', CustomerSignupAPIView.as_view(), name='customer-signup'),
    path('customer/update/', CustomerUpdateAPIView.as_view(), name='customer-update'),
]
