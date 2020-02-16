import os

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from home.models import Domain, Vendor

homepage = "https://esc.vn/"
urls = "https://esc.vn/bang-gia-ten-mien/"
source = "ESC"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"alt": "tên miền .vn"})
    mark_origin_parent = mark_origin.parent
    mark_origin_parent_sibling = mark_origin_parent.nextSibling
    origin_price = mark_origin_parent_sibling.string.strip("K") + ".000"
    sale_price = origin_price
    return [origin_price,sale_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("span", text=".COM.VN")
    mark_origin_sibling = mark_origin.nextSibling
    origin_price = mark_origin_sibling.string.strip(" K") + ".000"
    sale_price = origin_price
    return [origin_price,sale_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".com ")
    mark_origin_parent = mark_origin.parent
    mark_origin_parent_sibling = mark_origin_parent.nextSibling.nextSibling
    origin_price = mark_origin_parent_sibling.p.span.contents[2].string.strip()
    sale_price = origin_price
    return [origin_price,sale_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".net")
    mark_origin_parent = mark_origin.parent
    mark_origin_parent_sibling = mark_origin_parent.nextSibling.nextSibling
    origin_price = mark_origin_parent_sibling.p.span.string
    sale_price = origin_price
    return [origin_price,sale_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".org ")
    mark_origin_parent = mark_origin.parent
    mark_origin_parent_sibling = mark_origin_parent.nextSibling.nextSibling
    origin_price = mark_origin_parent_sibling.p.span.string
    sale_price = origin_price
    return [origin_price,sale_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".info ")
    mark_origin_parent = mark_origin.parent
    mark_origin_parent_sibling = mark_origin_parent.nextSibling.nextSibling
    origin_price = mark_origin_parent_sibling.p.span.contents[2].string.strip()
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
            objects = Domain.objects.filter(vendor=Vendor.objects.get(id=5), domain_type='vn')
            if objects.count() != 0:
                objects.delete()
            lst = get_vn()
            new_object = Domain.objects.create(vendor=Vendor.objects.get(id=5), domain_type='vn', origin_price=lst[0], sale_price=lst[1])

        def new_comvn():
            objects = Domain.objects.filter(vendor=Vendor.objects.get(id=5), domain_type='comvn')
            if objects.count() != 0:
                objects.delete()
            lst = get_comvn()
            new_object = Domain.objects.create(vendor=Vendor.objects.get(id=5), domain_type='comvn', origin_price=lst[0], sale_price=lst[1])
        def new_com():
            objects = Domain.objects.filter(vendor=Vendor.objects.get(id=5), domain_type='com')
            if objects.count() != 0:
                objects.delete()
            lst = get_com()
            new_object = Domain.objects.create(vendor=Vendor.objects.get(id=5), domain_type='com', origin_price=lst[0], sale_price=lst[1])
        def new_net():
            objects = Domain.objects.filter(vendor=Vendor.objects.get(id=5), domain_type='net')
            if objects.count() != 0:
                objects.delete()
            lst = get_net()
            new_object = Domain.objects.create(vendor=Vendor.objects.get(id=5), domain_type='net', origin_price=lst[0], sale_price=lst[1])
        def new_org():
            objects = Domain.objects.filter(vendor=Vendor.objects.get(id=5), domain_type='org')
            if objects.count() != 0:
                objects.delete()
            lst = get_org()
            new_object = Domain.objects.create(vendor=Vendor.objects.get(id=5), domain_type='org', origin_price=lst[0], sale_price=lst[1])
        def new_info():
            objects = Domain.objects.filter(vendor=Vendor.objects.get(id=5), domain_type='info')
            if objects.count() != 0:
                objects.delete()
            lst = get_info()
            new_object = Domain.objects.create(vendor=Vendor.objects.get(id=5), domain_type='info', origin_price=lst[0], sale_price=lst[1])
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

        
    

        