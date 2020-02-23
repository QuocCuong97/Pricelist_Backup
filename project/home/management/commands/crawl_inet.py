import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from home.models import Domain, Vendor

homepage = "https://inet.vn/"
urls = "https://inet.vn/api/domain/listsuffix"
source = "iNET"

def get_vn():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    origin_price = str(lst_json[0]['lePhiDangKy'] + lst_json[0]['phiDuyTri'] + lst_json[0]['qtdvNamDau'] * 110 // 100).rpartition('000')[0] + '.000'
    sale_price = origin_price
    return [origin_price,sale_price]

def get_comvn():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    origin_price = str(lst_json[2]['lePhiDangKy'] + lst_json[2]['phiDuyTri'] + lst_json[2]['qtdvNamDau'] * 110 // 100).rpartition('000')[0] + '.000'
    sale_price = origin_price
    return [origin_price,sale_price]

def get_com():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    origin_price = str(lst_json[1]['regOrigin']).rpartition('000')[0] + '.000'
    try:
        sale_price = str(lst_json[1]['regPromotion']).rpartition('000')[0] + '.000'
    except:
        sale_price = origin_price
    return [origin_price,sale_price]

def get_net():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    origin_price = str(lst_json[4]['regOrigin']).rpartition('000')[0] + '.000'
    try:
        sale_price = str(lst_json[4]['regPromotion']).rpartition('000')[0] + '.000'
    except:
        sale_price = origin_price
    return [origin_price,sale_price]

def get_org():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    origin_price = str(lst_json[6]['regOrigin']).rpartition('000')[0] + '.000'
    try:
        sale_price = str(lst_json[6]['regPromotion']).rpartition('000')[0] + '.000'
    except:
        sale_price = origin_price
    return [origin_price,sale_price]

def get_info():
    dom_origin = requests.get(urls).text
    lst_json = json.loads(dom_origin)
    origin_price = str(lst_json[9]['regOrigin']).rpartition('000')[0] + '.000'
    try:
        sale_price = str(lst_json[9]['regPromotion']).rpartition('000')[0] + '.000'
    except:
        sale_price = origin_price
    return [origin_price,sale_price]


class Command(BaseCommand):
    help = 'Crawl PriceList'


    def add_arguments(self, parser):
        parser.add_argument('-vn',action='store_true', help='crawl .vn')
        parser.add_argument('-comvn',action='store_true', help='crawl .com.vn')
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-org',action='store_true', help='crawl .org')
        parser.add_argument('-info',action='store_true', help='crawl .info')
        parser.add_argument('-a',action='store_true', help='crawl all')


    def handle(self, *args, **kwargs):
        def new_vn():
            lst = get_vn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='iNET'), domain_type='vn', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})

        def new_comvn():
            lst = get_comvn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='iNET'), domain_type='comvn', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='iNET'), domain_type='com', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='iNET'), domain_type='net', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='iNET'), domain_type='org', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='iNET'), domain_type='info', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        if kwargs['vn']:
            new_vn()
        elif kwargs['comvn']:
            new_comvn()
        elif kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['org']:
            new_org()
        elif kwargs['info']:
            new_info()
        elif kwargs['a']:
            new_vn()
            new_comvn()
            new_com()
            new_net()
            new_org()
            new_info()
        else:
            print("Invalid options! Please type '-h' for help")