from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    age = models.IntegerField()
    address = models.CharField(max_length=45)