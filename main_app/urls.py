from django.conf.urls import url
from .views import index, about, show, profile, sell_form, post_produce, marketplace, login_view, logout_view

urlpatterns = [
    url(r'^$', index),					# to main landing page
    url(r'^about/$', about),			# to about page
    url(r'^user/(\w+)/$', profile, name='profile'),				# display user profile page
    url(r'^marketplace/$', marketplace, name='marketplace'),	# display marketplace showing all produces available for sale
    url(r'^([0-9]+)/$', show, name='show'),						# display a single produce by id
    url(r'^sell/$', sell_form),									# display a sales template for a produce
    url(r'^sell/post_url/$', post_produce, name='post_produce'),# route to post a new produce up for sale
	url(r'^login/$', login_view, name='login'),		# display login page
	url(r'^logout/$', logout_view, name='logout'),	# route to logout
]