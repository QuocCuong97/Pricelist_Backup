from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/comodo.html')

def geotrust(request):
    return render(request, 'pages/geotrust.html')

def symantec(request):
    return render(request, 'pages/symantec.html')

def thawte(request):
    return render(request, 'pages/thawte.html')

def globalsign(request):
    return render(request, 'pages/globalsign.html')

def free(request):
    return render(request, 'pages/free.html')