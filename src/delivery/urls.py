from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from delivery import views

urlpatterns = [
    path('', views.DeliveryListAPIView.as_view(), name="delivery"),
    path('<int:pk>/', views.DeliveryCloseAPIView.as_view(), name="delivery_checkout"),
]

urlpatterns = format_suffix_patterns(urlpatterns)