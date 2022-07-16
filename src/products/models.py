from django.conf import settings
from django.db import models
from timestamps.models import Model

# Create your models here.
class Producer(Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productType = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    amount = models.CharField(max_length=100)