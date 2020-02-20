from django.shortcuts import render
from django.http import HttpResponse
from domain_price.models import Domain, Vendor

# Create your views here.

# def hosting(request):
#     return render(request, 'pages/hosting.html')

# def ssl(request):
#     return render(request, 'pages/ssl.html')

def index(request):
    lst_vn = Domain.objects.all().filter(domain_type='vn').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage')
    lst_comvn = Domain.objects.all().filter(domain_type='comvn').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage')
    lst_com = Domain.objects.all().filter(domain_type='com').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage')
    lst_net = Domain.objects.all().filter(domain_type='net').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage')
    lst_org = Domain.objects.all().filter(domain_type='org').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage')
    lst_info = Domain.objects.all().filter(domain_type='info').order_by('reg_promotion').values_list('reg_promotion', 'vendor__name', 'vendor__logo', 'vendor__homepage')

    count_vendor_vn = Domain.objects.all().filter(domain_type='vn').count() - 3
    count_vendor_comvn = Domain.objects.all().filter(domain_type='comvn').count() - 3
    count_vendor_com = Domain.objects.all().filter(domain_type='com').count() - 3
    count_vendor_net = Domain.objects.all().filter(domain_type='net').count() - 3
    count_vendor_org = Domain.objects.all().filter(domain_type='org').count() - 3
    count_vendor_info = Domain.objects.all().filter(domain_type='info').count() - 3
    

    lst_cheapest = [lst_com[0], lst_net[0], lst_org[0], lst_info[0], lst_comvn[0], lst_vn[0]]
    lst_second = [lst_com[1], lst_net[1], lst_org[1], lst_info[1], lst_comvn[1], lst_vn[1]]
    lst_third = [lst_com[2], lst_net[2], lst_org[2], lst_info[2], lst_comvn[2], lst_vn[2]]

    lst_com_other = []
    lst_net_other = []
    lst_org_other = []
    lst_info_other = []
    lst_comvn_other = []
    lst_vn_other = []

    for x in range(0, count_vendor_com):
        y = x + 3
        lst_com_other.append(lst_com[y])

    for x in range(0, count_vendor_net):
        y = x + 3
        lst_net_other.append(lst_net[y])

    for x in range(0, count_vendor_org):
        y = x + 3
        lst_org_other.append(lst_org[y])

    for x in range(0, count_vendor_info):
        y = x + 3
        lst_info_other.append(lst_info[y])

    for x in range(0, count_vendor_comvn):
        y = x + 3
        lst_comvn_other.append(lst_comvn[y])

    for x in range(0, count_vendor_vn):
        y = x + 3
        lst_vn_other.append(lst_vn[y])

    lst_count = [count_vendor_com, count_vendor_net, count_vendor_org, count_vendor_info, count_vendor_comvn, count_vendor_vn]
    lst_other = [lst_com_other, lst_net_other, lst_org_other, lst_info_other, lst_comvn_other, lst_vn_other]
        
    
    return render(request, 'pages/domain.html', {'lst_cheapest': lst_cheapest, 'lst_second': lst_second, 'lst_third': lst_third, 'lst_other': lst_other, 'lst_count': lst_count})

