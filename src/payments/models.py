from django.db import models
from django.utils.translation import ugettext_lazy as _
from timestamps.models import Model

class Payment(Model):
    user = models.ForeignKey("authentication.User", verbose_name=_("User"), on_delete=models.CASCADE)
    cart = models.OneToOneField("orders.Cart", verbose_name=_("Cart"), on_delete=models.CASCADE)
    card_number = models.CharField(_("Credit Card Number"), max_length=50)
    card_holder = models.CharField(_("Card Holder"), max_length=50)
    total_amount = models.DecimalField(_("Total Amount"), max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(_("Payment Date"), auto_now=False, auto_now_add=False)
