"""
URLs for ibl_app.
"""
from django.urls import path 
from .views import save_greeting 

urlpatterns = [
    path('greeting/', save_greeting, name='save_greeting'),
]
