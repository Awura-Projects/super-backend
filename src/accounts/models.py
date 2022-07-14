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

class Employee(Model):
    """
    Employee model to store employee information
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    birthdate = models.DateField(_("Birthdate"), auto_now=False, auto_now_add=False)

class Supplier(Model):
    """
    Supplier model to store supplier basic information
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
