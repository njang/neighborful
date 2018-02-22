from django.contrib import admin
from .models import Produce, Address, Balance

# Register your models here.
admin.site.register(Produce)
admin.site.register(Address)
admin.site.register(Balance)