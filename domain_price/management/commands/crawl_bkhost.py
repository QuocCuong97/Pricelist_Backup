import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Domain, Vendor

homepage = "https://bkhost.vn/"
urls = "https://bkhost.vn/ten-mien"
source = "BKHost"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark = dom_origin.find("td", text=".vn").parent
    mark_origin = mark.contents[3].string.rpartition('.000')[0] + '000'
    reg_origin = str(int(mark_origin) * 110 // 100)
    reg_promotion = reg_origin
    mark_renew = mark.contents[2].string.rpartition('.000')[0] + '000'
    renew_price = str(int(mark_renew) * 110 // 100)
    return [reg_origin, reg_promotion, renew_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark = dom_origin.find("td", text=".com.vn").parent
    mark_origin = mark.contents[3].string.rpartition('.000')[0] + '000'
    reg_origin = str(int(mark_origin) * 110 // 100)
    reg_promotion = reg_origin
    mark_renew = mark.contents[2].string.rpartition('.000')[0] + '000'
    renew_price = str(int(mark_renew) * 110 // 100)
    return [reg_origin, reg_promotion, renew_price]

def get_com():
    dom_origin = get_dom(urls)
    mark = dom_origin.find("td", text=".com").parent
    mark_reg = mark.contents[4].string.rpartition('.000')[0] + '000'
    reg_origin = str(int(mark_reg) * 110 // 100)
    reg_promotion = reg_origin
    mark_renew = mark.contents[3].string.rpartition('.000')[0] + '000'
    renew_price = str(int(mark_renew) * 110 // 100)
    mark_trans = mark.contents[2].string.rpartition('.000')[0] + '000'
    trans_price = str(int(mark_trans) * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_net():
    dom_origin = get_dom(urls)
    mark = dom_origin.find("td", text=".net").parent
    mark_reg = mark.contents[4].string.rpartition('.000')[0] + '000'
    reg_origin = str(int(mark_reg) * 110 // 100)
    reg_promotion = reg_origin
    mark_renew = mark.contents[3].string.rpartition('.000')[0] + '000'
    renew_price = str(int(mark_renew) * 110 // 100)
    mark_trans = mark.contents[2].string.rpartition('.000')[0] + '000'
    trans_price = str(int(mark_trans) * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_org():
    dom_origin = get_dom(urls)
    mark = dom_origin.find("td", text=".org").parent
    mark_reg = mark.contents[4].string.rpartition('.000')[0] + '000'
    reg_origin = str(int(mark_reg) * 110 // 100)
    reg_promotion = reg_origin
    mark_renew = mark.contents[3].string.rpartition('.000')[0] + '000'
    renew_price = str(int(mark_renew) * 110 // 100)
    mark_trans = mark.contents[2].string.rpartition('.000')[0] + '000'
    trans_price = str(int(mark_trans) * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_info():
    dom_origin = get_dom(urls)
    mark = dom_origin.find("td", text=".info").parent
    mark_reg = mark.contents[4].string.rpartition('.000')[0] + '000'
    reg_origin = str(int(mark_reg) * 110 // 100)
    reg_promotion = reg_origin
    mark_renew = mark.contents[3].string.rpartition('.000')[0] + '000'
    renew_price = str(int(mark_renew) * 110 // 100)
    mark_trans = mark.contents[2].string.rpartition('.000')[0] + '000'
    trans_price = str(int(mark_trans) * 110 // 100)
    return [reg_origin, reg_promotion, renew_price, trans_price]

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
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKHost'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_comvn():
            lst = get_comvn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKHost'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKHost'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKHost'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKHost'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='BKHost'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
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
