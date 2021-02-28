
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.Fetch,name="Home"),
    path('events', views.Fetch,name="Events"),
    path('Destination',views.Destination)

    
]
