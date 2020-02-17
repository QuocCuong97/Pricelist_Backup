import os

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from home.models import Domain, Vendor

homepage = "https://vhost.vn/"
urls = "https://vhost.vn/ten-mien/"
source = "VHost"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"id": "ptiv8s0NDNac"})
    mark_origin_content = mark_origin.tbody.contents[7].contents[2]
    origin_price = mark_origin_content.text.strip(" VND").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]
    
def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"id": "ptiv8s0NDNac"})
    mark_origin_content = mark_origin.tbody.contents[1].contents[2]
    origin_price = mark_origin_content.text.strip(" VND").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]
    
def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"id": "ptiv8s0NDNac"})
    mark_origin_content = mark_origin.tbody.contents[8].contents[2]
    origin_price = mark_origin_content.text.strip(" VND").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]
    
def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"id": "ptiv8s0NDNac"})
    mark_origin_content = mark_origin.tbody.contents[2].contents[2]
    origin_price = mark_origin_content.text.strip(" VND").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]
    
def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"id": "ptiv8s0NDNac"})
    mark_origin_content = mark_origin.tbody.contents[3].contents[2]
    origin_price = mark_origin_content.text.strip(" VND").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"id": "ptiv8s0NDNac"})
    mark_origin_content = mark_origin.tbody.contents[5].contents[2]
    origin_price = mark_origin_content.text.strip(" VND").replace(",", ".")
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
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(id=8), domain_type='vn', origin_price=lst[0], sale_price=lst[1])

        def new_comvn():
            lst = get_comvn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(id=8), domain_type='comvn', origin_price=lst[0], sale_price=lst[1])
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(id=8), domain_type='com', origin_price=lst[0], sale_price=lst[1])
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(id=8), domain_type='net', origin_price=lst[0], sale_price=lst[1])
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(id=8), domain_type='org', origin_price=lst[0], sale_price=lst[1])
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(id=8), domain_type='info', origin_price=lst[0], sale_price=lst[1])
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

        
    

        