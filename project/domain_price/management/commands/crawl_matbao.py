import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Domain, Vendor

homepage = "https://www.matbao.net/"
urls = "https://www.matbao.net/ten-mien/bang-gia-ten-mien.html"
source = "MatBao"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("u", text=".vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    reg_origin = mark_origin_parent.contents[11].text.strip("\n đ")
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .vn'})
    mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
    reg_promotion = mark_sale_content[0].strip()
    return [reg_origin, reg_promotion]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.com.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[3]
    reg_origin = mark_origin_parent_content.text.strip().strip(' đ')
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .com'})
    mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
    reg_promotion = mark_sale_content[0].strip()
    return [reg_origin, reg_promotion]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("u", text=".net.vn/ .biz.vn/ .com.vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    reg_origin = mark_origin_parent.contents[11].text.strip("\n đ")
    try:
        dom_sale = get_dom(homepage)
        mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .com.vn'})
        mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
        reg_promotion = mark_sale_content[0].strip()
    except:
        reg_promotion = reg_origin
    return [reg_origin, reg_promotion]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.net.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[3]
    reg_origin = mark_origin_parent_content.text.strip().strip(' đ')
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .net'})
    mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
    reg_promotion = mark_sale_content[0].strip()
    return [reg_origin, reg_promotion]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.org.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[1]
    reg_origin = mark_origin_parent_content.text.strip().strip(' đ')
    try:
        dom_sale = get_dom(homepage)
        mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .org'})
        mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
        reg_promotion = mark_sale_content[0].strip()
    except:
        reg_promotion = reg_origin
    return [reg_origin, reg_promotion]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.info.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[3]
    reg_origin = mark_origin_parent_content.text.strip().strip(' đ')
    try:
        dom_sale = get_dom(homepage)
        mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .info'})
        mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
        reg_promotion = mark_sale_content[0].strip()
    except:
        reg_promotion = reg_origin
    return [reg_origin, reg_promotion]

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
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_comvn():
            lst = get_comvn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='MatBao'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1]})
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