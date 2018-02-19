from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Produce
from .forms import ProduceForm, LoginForm

# Create your views here.
def index(request):
	return render(request, 'index.html')

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

def delete_post(request, produce_id):
    Produce.objects.get(id=produce_id).delete()
    return HttpResponseRedirect('/marketplace')

def post_produce(request):
    form = ProduceForm(request.POST)
    if form.is_valid():
        produce = form.save(commit = False)
        produce.seller = request.user
        produce.buyer = ''
        produce.save()
    return HttpResponseRedirect('/marketplace')

def edit_form(request, produce_id):
    produce = Produce.objects.get(id=produce_id)
    form = ProduceForm({'name': produce.name, 'price': produce.price, 'quantity': produce.quantity, 'user':produce.seller})
    return render(request, 'edit.html', {'form': form})

def update_produce(request, produce_id):
    form = ProduceForm(request.POST)
    if form.is_valid():
        produce = form.save(commit = False)
        produce.id = produce_id
        produce.seller = request.user
        produce.save()
    return HttpResponseRedirect('/marketplace')

def profile(request, username):
    user = User.objects.get(username=username)
    produces = Produce.objects.filter(seller=user)
    return render(request, 'profile.html', {'user': user, 'produces': produces})

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')