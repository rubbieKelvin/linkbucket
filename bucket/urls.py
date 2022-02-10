from django.urls import path
from .views import ListCreateLinkApiView

url_patterns = [
    path('links/', ListCreateLinkApiView.as_view())
]