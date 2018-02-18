from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Produce
from .form import ProduceForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def marketplace(request):
	produces = Produce.objects.all()
	return render(request, 'marketplace.html', {'produces': produces})

def about(request):
	return render(request, 'about.html')

def show(request, produce_id):
    produce = Produce.objects.get(id=produce_id)
    return render(request, 'show.html', {'produce': produce}) 

def sell_form(request):
    form = ProduceForm()
    return render(request, 'sell.html', {'form': form})

def post_produce(request):
    form = ProduceForm(request.POST)
    if form.is_valid():
        produce = form.save(commit = False)
        produce.user = request.user
        produce.save()
    return HttpResponseRedirect('/marketplace')

def profile(request, username):
    user = User.objects.get(username=username)
    produces = Produce.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'produces': produces})