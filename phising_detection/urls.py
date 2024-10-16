from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Simple homepage view
def home(request):
    return HttpResponse("<h1>Welcome to Phishing Detection App</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('detection.urls')),  # API routes
    path('', home),  # Root URL (homepage)
]
