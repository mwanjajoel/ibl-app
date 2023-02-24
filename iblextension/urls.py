"""
URLs for ibl_app.
"""
from django.contrib import admin
from django.urls import path, include
from .views import save_greeting 

urlpatterns = [
    path('greeting/', save_greeting, name='save_greeting'),
]
