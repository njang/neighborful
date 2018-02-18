from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Produce
from .form import ProduceForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

def marketplace(request):
	produces = Produce.objects.all()
	return render(request, 'marketplace.html', {'produces': produces})

def about(request):
	return render(request, 'about.html')

def sell(request):
    form = ProduceForm(request.POST)
    if form.is_valid():
        produce = form.save(commit = False)
        # produce.user = request.user
        produce.save()
    return render(request, 'sell.html')
    # return HttpResponseRedirect('/')
