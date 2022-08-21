from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                'producer',
                'posted_by',
                'product_name',
                'product_type',
                'description',
                'amount',
                'price',
                'discount',
            ),
        }),
    )

# @admin.register(Producer)
# class ProducerAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             "fields": (
#                 'title',
#             ),
#         }),
#     )
