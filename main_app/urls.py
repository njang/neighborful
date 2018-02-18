from django.urls import include, path
from .views import index, about, sell, marketplace

urlpatterns = [
    path(r'', index),
    path(r'about/', about),
    path(r'marketplace/', marketplace),
]