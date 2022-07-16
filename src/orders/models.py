from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from timestamps.models import Model

class Cart(Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Customer"),
        on_delete=models.CASCADE
    )
    order_date = models.DateTimeField(_("Order Date"), auto_now_add=True)
    delivery_man = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Delivery Man"),
        on_delete=models.CASCADE,
        related_name='delivery_man',
        blank=True, null=True
    )
    closed = models.BooleanField(_("Status"), default=False)
    closed_time = models.DateTimeField(
        _("Closed Time"), auto_now=False,
        auto_now_add=False, blank=True,
        null=True
    )
    def clean(self):
        delivery_man = self.delivery_man

        if delivery_man.user_type != 'delivery':
            raise ValidationError(
                {
                    'delivery_man': 'User must be a delivery man'
                }
            )

class CartItem(Model):
    cart = models.ForeignKey(
        "orders.Cart",
        verbose_name=_("Cart"),
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        "products.Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(_("Quantity"))
    unit_price = models.DecimalField(_("Unit Price"), max_digits=6, decimal_places=2)
    discount = models.DecimalField(_("Discount"), max_digits=3, decimal_places=2)

    def clean(self):
        discount = self.discount
        if discount < 0:
            raise ValidationError(
                {
                    'discount': 'Discount cannot be negative number'
                }
            )
