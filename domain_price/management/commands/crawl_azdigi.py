import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Domain, Vendor

homepage = "https://azdigi.com/"
urls = "https://azdigi.com/dang-ky-ten-mien/"
source = "AZDIGI"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.com')
    mark_origin_sibling = mark_origin.parent.nextSibling
    reg_origin = mark_origin_sibling.string.strip(' đ')
    reg_promotion = reg_origin
    return [reg_origin,reg_promotion]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.net')
    mark_origin_sibling = mark_origin.parent.nextSibling
    reg_origin = mark_origin_sibling.string.strip(' đ')
    reg_promotion = reg_origin
    return [reg_origin,reg_promotion]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.info')
    mark_origin_sibling = mark_origin.parent.nextSibling
    reg_origin = mark_origin_sibling.string.strip(' đ')
    reg_promotion = reg_origin
    return [reg_origin,reg_promotion]


class Command(BaseCommand):
    help = 'Crawl PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-info',action='store_true', help='crawl .info')
        parser.add_argument('-a',action='store_true', help='crawl all')
    

    def handle(self, *args, **kwargs):
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='AZDIGI'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='AZDIGI'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='AZDIGI'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        if kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['info']:
            new_info()
        elif kwargs['a']:
            new_com()
            new_net()
            new_info()
        else:
            print("Invalid options! Please type '-h' for help")