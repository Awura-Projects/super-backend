from django.urls import path, include

from .views import (
    CustomerSignupAPIView, CustomerUpdateAPIView,
    PasswordChangeAPIView, CustomerRetrieveAPIView,
    UserRetrieveAPIView
)

urlpatterns = [
    path('', include("accounts.routers")),
    path('account/', UserRetrieveAPIView.as_view(), name='account-detail'),
    path('change-password/', PasswordChangeAPIView.as_view(), name='change-password'),
    path('customer/signup/', CustomerSignupAPIView.as_view(), name='customer-signup'),
    path('customer/update/', CustomerUpdateAPIView.as_view(), name='customer-update'),
]
