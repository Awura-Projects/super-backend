from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.products_form, name= 'product_insert'), #get and post req, for insert operations
    path('<int:id>/', views.products_form, name=  'product_update'), #get and post req, for update operations
    path('list/', views.product_list, name= 'product_list'), #get req to retrieve and display data
    path('delete/<int:id>/', views.product_delete, name= 'product_delete'),
]