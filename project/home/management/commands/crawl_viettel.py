import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from home.models import Domain, Vendor

homepage = "https://viettelidc.com.vn/"
urls = "https://viettelidc.com.vn/ten-mien-domain"
source = "Viettel IDC"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("strong", text=".vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[11]
    origin_price = mark_origin_parent_content.div.strong.string.strip(' đ')
    sale_price = origin_price
    return [origin_price, sale_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("strong", text=".com.vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[11]
    origin_price = mark_origin_parent_content.div.strong.string.strip(' đ')
    sale_price = origin_price
    return [origin_price, sale_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("strong", text=".com")
    mark_origin_parent = mark_origin.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[7].div.strong.string.strip(' đ').rpartition('.000')[0] + '000'
    mark_origin_parent_content_split = str(int(mark_origin_parent_content) * 110 // 100)
    origin_price = mark_origin_parent_content_split[:-3] + '.' + mark_origin_parent_content_split[-3:]
    sale_price = origin_price
    return [origin_price, sale_price]

def get_net_org_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("strong", text=".net .org .info")
    mark_origin_parent = mark_origin.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[7].div.strong.string.strip(' đ').rpartition('.000')[0] + '000'
    mark_origin_parent_content_split = str(int(mark_origin_parent_content) * 110 // 100)
    origin_price = mark_origin_parent_content_split[:-3] + '.' + mark_origin_parent_content_split[-3:]
    sale_price = origin_price
    return [origin_price, sale_price]


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
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Viettel IDC'), domain_type='vn', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})

        def new_comvn():
            lst = get_comvn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Viettel IDC'), domain_type='comvn', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Viettel IDC'), domain_type='com', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_net():
            lst = get_net_org_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Viettel IDC'), domain_type='net', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_org():
            lst = get_net_org_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Viettel IDC'), domain_type='org', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_info():
            lst = get_net_org_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='Viettel IDC'), domain_type='info', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
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