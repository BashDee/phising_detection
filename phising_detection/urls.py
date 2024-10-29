from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render


# Simple homepage view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('detection.urls')),  # API routes
    path('', lambda request: render(request, 'index.html')),  # Serve index.html on root URL
]
