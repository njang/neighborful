from django.db import models
from django.contrib.auth.models import User


#Manage the model
class ProduceManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(ProduceManager, self)

class Produce(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='seller')
    # buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='buyer')
    buyer = models.CharField(max_length=100)
    objects = ProduceManager()

    def __str__(self):
    	return self.name

class Meta:
    ordering = ["-id", "-timestamp", "-updated"]

    def __str__(self):
    	return self.name

class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=100)
    gps_lat = models.DecimalField(max_digits=10, decimal_places=6)
    gps_lng = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
    	return self.street

