from django.urls import path

from accounts.admin_routers import router as accounts_router
from orders.admin_routers import router as orders_router
from payments.admin_routers import router as payments_router

urlpatterns = []

urlpatterns += accounts_router.urls
urlpatterns += orders_router.urls
urlpatterns += payments_router.urls
