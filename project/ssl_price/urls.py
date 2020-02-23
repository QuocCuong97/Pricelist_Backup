from django.urls import path
from . import views

urlpatterns = [
    path('comodo/', views.index),
    path('geotrust/', views.geotrust),
    path('symantec/', views.symantec),
    path('thawte/', views.thawte),
    path('globalsign', views.globalsign),
    path('freessl/', views.free),
]