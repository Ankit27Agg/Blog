from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home')
    path('contact', views.home, name='home')
    path('about', views.home, name='home')
]
