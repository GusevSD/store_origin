from django.contrib import admin
from django.urls import path, include
from store_origin import views

urlpatterns = [
    path('', views.index),
]
