import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from home.models import Domain, Vendor

homepage = "https://vn.godaddy.com/"
urls = "https://vn.godaddy.com/domains/domain-name-search"
source = "GoDaddy"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('strong', text='.com')
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[7].div.p.span
    origin_price = mark_origin_parent_content.string[:-2]
    sale_price = origin_price
    note = "Yêu cầu mua 2 năm. Thanh toán cho năm thứ hai với giá 378.000"
    return [origin_price, sale_price, note]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('strong', text='.org')
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[7].div.p.span
    origin_price = mark_origin_parent_content.string[:-2]
    sale_price = origin_price
    return [origin_price, sale_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('strong', text='.net')
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[7].div.p.span
    origin_price = mark_origin_parent_content.string[:-2]
    sale_price = origin_price
    return [origin_price, sale_price]


class Command(BaseCommand):
    help = 'Crawl PriceList'

    def add_arguments(self, parser):
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-org',action='store_true', help='crawl .org')
        parser.add_argument('-a',action='store_true', help='crawl all')

    def handle(self, *args, **kwargs):
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='GoDaddy'), domain_type='com', defaults = {'origin_price': lst[0], 'sale_price': lst[1], 'note': lst[2]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='GoDaddy'), domain_type='net', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='GoDaddy'), domain_type='org', defaults = {'origin_price': lst[0], 'sale_price': lst[1]})
        if kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['org']:
            new_org()
        elif kwargs['a']:
            new_com()
            new_net()
            new_org()
        else:
            print("Invalid options! Please type '-h' for help")