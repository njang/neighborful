from django.db import models
from django.contrib.auth.models import User

class Produce(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
    	return self.name