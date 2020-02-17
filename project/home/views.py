from django.shortcuts import render
from django.http import HttpResponse
from home.models import Domain, Vendor
# from .models import Vendor
# Create your views here.

# def index(request):
#     return render(request, 'pages/domain.html')

def hosting(request):
    return render(request, 'pages/hosting.html')

def vps(request):
    return render(request, 'pages/vps.html')

def index(request):
    lst_vn = Domain.objects.all().filter(domain_type='vn').order_by('sale_price').values_list('sale_price')
    lst_comvn = Domain.objects.all().filter(domain_type='comvn').order_by('sale_price').values_list('sale_price')
    lst_com = Domain.objects.all().filter(domain_type='com').order_by('sale_price').values_list('sale_price')
    lst_net = Domain.objects.all().filter(domain_type='net').order_by('sale_price').values_list('sale_price')
    lst_org = Domain.objects.all().filter(domain_type='org').order_by('sale_price').values_list('sale_price')
    lst_info = Domain.objects.all().filter(domain_type='info').order_by('sale_price').values_list('sale_price')

    lst_cheapest = [lst_com[0], lst_net[0], lst_org[0], lst_info[0], lst_comvn[0], lst_vn[0]]
    lst_second = [lst_com[1], lst_net[1], lst_org[1], lst_info[1], lst_comvn[1], lst_vn[1]]
    lst_third = [lst_com[2], lst_net[2], lst_org[2], lst_info[2], lst_comvn[2], lst_vn[2]]
    return render(request, 'pages/domain.html', {'lst_cheapest': lst_cheapest, 'lst_second': lst_second, 'lst_third': lst_third})

