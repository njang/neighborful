from django.shortcuts import render
from django.http import HttpResponse
from .models import Produce

# Create your views here.
def index(request):
	return render(request, 'index.html')

def marketplace(request):
	produces = Produce.objects.all()
	return render(request, 'marketplace.html', {'produces': produces})

def about(request):
	return render(request, 'about.html')
