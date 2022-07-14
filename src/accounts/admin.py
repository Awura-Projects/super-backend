from django.contrib import admin

from .models import Employee, Supplier, Delivery

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass
