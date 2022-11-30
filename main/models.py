from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.IntegerField()