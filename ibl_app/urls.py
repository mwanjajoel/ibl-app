"""
URLs for ibl_app.
"""
from django.contrib import admin
from django.urls import path, include
from .views import save_greeting 

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/greeting/', save_greeting, name='save_greeting'),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
