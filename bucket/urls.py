from django.urls import path
from .views import ListCreateLinkApiView

urlpatterns = [
    path('links/', ListCreateLinkApiView.as_view())
]