from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from timestamps.models import Model

class Employee(Model):
    """
    Employee model to store employee information
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(_("Profile Picture"), upload_to='accounts/employee/profile_pictures/')
    birthdate = models.DateField(_("Birthdate"), auto_now=False, auto_now_add=False)
    identification_card = models.ImageField(_("Id Card"), upload_to='accounts/employee/id/')

class Supplier(Model):
    """
    Supplier model to store supplier basic information
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(_("Profile Picture"), upload_to='accounts/supplier/profile_pictures/')
    birthdate = models.DateField(_("Birthdate"), auto_now=False, auto_now_add=False)
    identification_card = models.ImageField(_("Id Card"), upload_to='accounts/supplier/id/')

class Delivery(Model):
    """
    Delivery model to store supplier basic information
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(_("Profile Picture"), upload_to='accounts/delivery/profile_pictures/')
    birthdate = models.DateField(_("Birthdate"), auto_now=False, auto_now_add=False)
    identification_card = models.ImageField(_("Id Card"), upload_to='accounts/delivery/id/')
