import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Domain, Vendor

homepage = "https://www.pavietnam.vn/"
urls = "https://www.pavietnam.vn/en/ten-mien-bang-gia.html"
sale_url = "https://www.pavietnam.vn/en/uu-dai-ten-mien-viet-nam.html"
source = "P.A VietNam"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_sale = get_dom(sale_url)
    mark_sale = dom_sale.find("strong", text=".VN")
    reg_promotion = mark_sale.nextSibling.nextSibling.string + ".000"
    reg_origin = mark_sale.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.strong.string + ".000"
    return [reg_origin,reg_promotion]

def get_comvn():
    dom_sale = get_dom(sale_url)
    mark_sale = dom_sale.find("strong", text=".COM.VN")
    reg_promotion = mark_sale.nextSibling.nextSibling.string + ".000"
    reg_origin = mark_sale.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.strong.string + ".000"
    return [reg_origin,reg_promotion]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "com"})
    mark_origin_parent = mark_origin.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5]
    reg_origin = mark_origin_parent_content.contents[1].text.strip("d")
    reg_promotion = reg_origin
    return [reg_origin,reg_promotion]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "net"})
    mark_origin_parent = mark_origin.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5]
    reg_origin = mark_origin_parent_content.contents[1].text.strip("d")
    reg_promotion = reg_origin
    return [reg_origin,reg_promotion]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "org"})
    mark_origin_parent = mark_origin.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5]
    reg_origin = mark_origin_parent_content.contents[1].text.strip("d")
    reg_promotion = reg_origin
    return [reg_origin,reg_promotion]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('span', attrs={"id": "info"})
    mark_origin_parent = mark_origin.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5]
    reg_origin = mark_origin_parent_content.contents[1].text.strip("d")
    reg_promotion = reg_origin
    return [reg_origin,reg_promotion]


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
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})

        def new_comvn():
            lst = get_comvn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
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

        