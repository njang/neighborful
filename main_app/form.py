from django import forms
from .models import Produce

class ProduceForm(forms.ModelForm):
	class Meta:
		model = Produce
		fields = ['name', 'price', 'quantity', 'location']

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())