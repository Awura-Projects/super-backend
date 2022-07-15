from django.urls import path, include

from .views import (
    CustomerSignupAPIView, CustomerUpdateAPIView,
    PasswordChangeAPIView
)

urlpatterns = [
    path('', include("accounts.routers")),
    path('change-password/', PasswordChangeAPIView.as_view(), name='change-password'),
    path('customer/signup/', CustomerSignupAPIView.as_view(), name='customer-signup'),
    path('customer/update/', CustomerUpdateAPIView.as_view(), name='customer-update'),
]
