from django import forms
from .models import Produce, Address

class ProduceForm(forms.ModelForm):
	class Meta:
		model = Produce
		fields = ['name', 'price', 'quantity']

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ['street']
