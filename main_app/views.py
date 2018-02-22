from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.db.models import Q
from .models import Produce, Address
from .forms import ProduceForm, LoginForm, AddressForm
from django.utils import timezone
from statistics import mean

import os
import requests

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

# Create your views here.
def index(request):
	return render(request, 'index.html')

def marketplace(request):
	produces = Produce.objects.all()
	return render(request, 'marketplace.html', {'produces': produces})

def search(request):
	today = timezone.now().date()
	queryset_list = Produce.objects.active() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Produce.objects.all()

	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(seller__first_name__icontains=query) |
				Q(seller__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 3) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
		"query": query,
	}

	return render(request, 'search.html', context)

def maps(request):
    addresses = Address.objects.all()
    center_lat = mean(address.gps_lat for address in addresses)
    center_lng = mean(address.gps_lng for address in addresses)
    # key = os.environ["GOOGLE_MAPS_API_KEY"]
    # return render(request, 'maps.html', {'addresses': addresses, 'center_lat': center_lat, 'center_lng': center_lng, 'key': key})
    return render(request, 'maps.html', {'addresses': addresses, 'center_lat': center_lat, 'center_lng': center_lng})

def about(request):
	return render(request, 'about.html')

def show(request, produce_id):
    produce = Produce.objects.get(id=produce_id)
    return render(request, 'show.html', {'produce': produce})

def sell_form(request):
    form = ProduceForm()
    return render(request, 'sell.html', {'form': form})

def address_form(request):
    form = AddressForm()
    return render(request, 'address.html', {'form': form})

def update_address(request):
    form = AddressForm(request.POST)
    if form.is_valid():
        address = form.save(commit = False)
        # Prepare for Google Maps geocode API
        params = {
            'address': address.street,
            'sensor': 'false',
            'region': 'us'
        }

        # Make the request and get the response data
        req = requests.get(GOOGLE_MAPS_API_URL, params=params)
        res = req.json()

        # Use the first result
        result = res['results'][0]

        # Save the result into the address database
        address.user = request.user
        address.street = result['formatted_address']
        address.gps_lat = result['geometry']['location']['lat']
        address.gps_lng = result['geometry']['location']['lng']
        address.save()
    return_to = '/'
    return HttpResponseRedirect('/maps')

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
    return render(request, 'edit.html', {'form': form, 'produce':produce})

def update_produce(request, produce_id):
    form = ProduceForm(request.POST)
    if form.is_valid():
        produce = form.save(commit = False)
        produce.id = produce_id
        produce.seller = request.user
        produce.save()
    return HttpResponseRedirect('/marketplace')

def buy_produce(request, produce_id):
    form = ProduceForm(request.POST)
    if form.is_valid():
        produce = form.save(commit = False)
        produce.id = produce_id
        produce.buyer = request.user
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
