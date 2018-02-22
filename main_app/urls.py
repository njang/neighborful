from django.conf.urls import url
from .views import index, about, maps, show, profile, sell_form, address_form, update_address, edit_form, post_produce, buy_produce, update_produce, delete_post, marketplace, login_view, logout_view, search

urlpatterns = [
    url(r'^$', index),					# to main landing page
    url(r'^about/$', about),            # to about page
    url(r'^maps/$', maps),			       # to maps page
    url(r'^search/$', search),
    url(r'^user/(\w+)/$', profile, name='profile'),				# display user profile page
    url(r'^marketplace/$', marketplace, name='marketplace'),	# display marketplace showing all produces available for sale
    url(r'^([0-9]+)/$', show, name='show'),						# display a single produce by id
    url(r'^sell/$', sell_form),                                 # display a sales template for a produce
    url(r'^sell/post_url/$', post_produce, name='post_produce'),# route to post a new produce up for sale
    url(r'^address/$', address_form),                                   # display a sales template for a produce
    url(r'^address/post_url/$', update_address, name='update_address'),                                   # display a sales template for a produce
    url(r'^edit/([0-9]+)/$', edit_form, name='edit'),           # display a single produce by id
    url(r'^edit/([0-9]+)/update/$', update_produce, name='edit'),  # edit a single produce by id
    url(r'^([0-9]+)/buy/$', buy_produce, name='buy'),  # edit a single produce by id
    url(r'^delete/([0-9]+)/$', delete_post, name='delete'),  # delete a single produce by id
	url(r'^login/$', login_view, name='login'),		# display login page
	url(r'^logout/$', logout_view, name='logout'),	# route to logout
]
