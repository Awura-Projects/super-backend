
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# class Producer(models.Model):
#     title = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title


class Product(models.Model):
    producer = models.ForeignKey("accounts.Supplier", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='Images/', default='Images/None/No-img.jpg')
    doc = models.FileField(upload_to='Doc/', default='Doc/None/No-doc.pdf')
    posted_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    amount = models.PositiveIntegerField(_("Amount"))
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)
    discount = models.DecimalField(
        _("Discount"), max_digits=3, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.posted_by.first_name} {self.posted_by.last_name}'
