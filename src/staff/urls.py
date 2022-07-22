from django.urls import path

from accounts.admin_routers import router as account_router
from orders.admin_routers import router as order_router
from payments.admin_routers import router as payment_router

urlpatterns = []

urlpatterns += payment_router.urls
urlpatterns += order_router.urls
urlpatterns += account_router.urls
