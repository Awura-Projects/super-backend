from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from timestamps.models import Model

class Customer(Model):
    """
    Customer model to store customer's information
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    address = models.CharField(_("City"), max_length=250)
