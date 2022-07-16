from django.db import models
from timestamps.models import Model

# Create your models here.
class Producer(Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product(Model):
    productName = models.CharField(max_length=100)
    productType = models.CharField(max_length=100)
    Description = models.TextField(max_length=100)
    Amount = models.CharField(max_length=100)
    producer= models.ForeignKey(Producer,on_delete=models.CASCADE)