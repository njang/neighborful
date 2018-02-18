from django.conf.urls import url
from .views import index, about, show, profile, sell_form, post_produce, dashboard, marketplace

urlpatterns = [
    url(r'^$', index),
    url(r'^about/$', about),
    url(r'^dashboard/$', dashboard),
    url(r'^user/(\w+)/$', profile, name='profile'),
    url(r'^marketplace/$', marketplace, name='marketplace'),
    url(r'^([0-9]+)/$', show, name="show"),
    url(r'^sell/$', sell_form),
    url(r'^sell/post_url/$', post_produce, name='post_produce'),
]