from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hosting', views.hosting),
    path('vps', views.vps)
]