from django.db import models
from django.contrib.auth.models import User

class Produce(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    seller = models.ForeignKey(User, on_delete=models.PROTECT)
    buyer = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.name
    	