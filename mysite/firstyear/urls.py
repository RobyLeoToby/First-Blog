from django.contrib import admin
from django.urls import path
from .views import render
from . import views

urlpatterns = [
    path('firstyear/', views.index, name='firstyear'),
]