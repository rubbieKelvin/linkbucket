from django.urls import path
from . import views

urlpatterns = [
    path('links/fetch/', views.get_links),
    path("links/create/", views.create_link),
    path('i/<str:tid>/', views.open_link),
    path('link/<str:tid>/upvote/', views.up_vote),
    path('link/<str:tid>/downvote/', views.down_vote),
]