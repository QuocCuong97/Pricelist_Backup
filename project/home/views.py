from django.shortcuts import render
from django.http import HttpResponse
# from .models import Vendor
# Create your views here.

def index(request):
    return render(request, 'pages/domain.html')

def hosting(request):
    return render(request, 'pages/hosting.html')

def vps(request):
    return render(request, 'pages/vps.html')
# def list(request):
#     Data = {"Vendor": Vendor.objects.all()}
#     return render(request, 'pages/home.html', Data)

