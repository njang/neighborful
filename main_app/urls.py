from django.urls import include, path
from .views import index, about, marketplace

urlpatterns = [
    path(r'', index),
    path(r'about/', about),
    path(r'marketplace/', marketplace),
]