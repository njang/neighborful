from django.urls import include, path
from .views import index, about

urlpatterns = [
    path(r'', index),
    path(r'about/', about),
]