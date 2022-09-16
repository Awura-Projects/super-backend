from django.urls import path

from .views import (
    CustomerSignupAPIView, CustomerUpdateAPIView,
    PasswordChangeAPIView, UserRetrieveAPIView,
    UserUpdateAPIView, AccountRetrieveAPIView,
    ForgotPasswordAPIView, PasswordResetAPIView
)

urlpatterns = [
    path('account/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('account/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('account/<int:pk>/', AccountRetrieveAPIView.as_view(),
         name='account-detail'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('reset-password/<slug:uid>/<slug:token>/',
         PasswordResetAPIView.as_view(), name='reset-password'),
    path('change-password/', PasswordChangeAPIView.as_view(), name='change-password'),
    path('customer/signup/', CustomerSignupAPIView.as_view(), name='customer-signup'),
    path('customer/update/', CustomerUpdateAPIView.as_view(), name='customer-update'),
]
