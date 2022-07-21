from django.urls import path

from payments.routers import router as payment_router

urlpatterns = []

urlpatterns += payment_router.urls
