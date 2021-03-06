import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Domain, Vendor

homepage = "https://esc.vn/"
urls = "https://esc.vn/bang-gia-ten-mien/"
source = "ESC"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.vn').parent.parent
    reg_origin = str(round(float(mark_origin.contents[1].text) + float(mark_origin.contents[2].text) + float(mark_origin.contents[3].text) * 110 // 100)) + '000'
    try:
        dom_promotion = get_dom(homepage)
        mark_promotion = dom_promotion.find(attrs={'alt': 'tên miền .vn'}).parent
        reg_promotion = mark_promotion.nextSibling.string.replace('K', '000')
    except:
        reg_promotion = reg_origin
    renew_price = str(round(float(mark_origin.contents[2].text) + float(mark_origin.contents[4].text) * 110 // 100)) + '000'
    trans_price = str(round(float(mark_origin.contents[5].text) + float(mark_origin.contents[6].text) * 110 // 100)) + '000'
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('p', text='.net.vn/ .com.vn/ .biz.vn').parent.parent
    reg_origin = str(round(float(mark_origin.contents[1].text) + float(mark_origin.contents[2].text) + float(mark_origin.contents[3].text) * 110 // 100)) + '000'
    try:
        dom_promotion = get_dom(homepage)
        mark_promotion = dom_promotion.find('span', text='.COM.VN')
        reg_promotion = mark_promotion.nextSibling.string.replace('K', '000')
    except:
        reg_promotion = reg_origin
    renew_price = str(round(float(mark_origin.contents[2].text) + float(mark_origin.contents[4].text) * 110 // 100)) + '000'
    trans_price = str(round(float(mark_origin.contents[5].text) + float(mark_origin.contents[6].text) * 110 // 100)) + '000'
    return [reg_origin, reg_promotion, renew_price, trans_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".com ").parent.parent
    try:
        reg_promotion = mark_origin.contents[2].font.string.strip().replace('.', '')
        reg_origin = mark_origin.contents[2].strike.string.strip().replace('.', '')
        renew_price = reg_origin
    except:
        reg_origin = mark_origin.contents[2].span.string.strip().replace('.', '')
        reg_promotion = reg_origin
        renew_price = reg_origin
    return [reg_origin, reg_promotion, renew_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".net").parent.parent
    try:
        reg_promotion = mark_origin.contents[2].font.string.strip().replace('.', '')
        reg_origin = mark_origin.contents[2].strike.string.strip().replace('.', '')
        renew_price = reg_origin
    except:
        reg_origin = mark_origin.contents[2].span.string.strip().replace('.', '')
        reg_promotion = reg_origin
        renew_price = reg_origin
    return [reg_origin, reg_promotion, renew_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".org ").parent.parent
    try:
        reg_promotion = mark_origin.contents[2].font.string.strip().replace('.', '')
        reg_origin = mark_origin.contents[2].strike.string.strip().replace('.', '')
        renew_price = reg_origin
    except:
        reg_origin = mark_origin.contents[2].span.string.strip().replace('.', '')
        reg_promotion = reg_origin
        renew_price = reg_origin
    return [reg_origin, reg_promotion, renew_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("p", text=".info ").parent.parent
    try:
        reg_promotion = mark_origin.contents[2].font.string.strip().replace('.', '')
        reg_origin = mark_origin.contents[2].strike.string.strip().replace('.', '')
        renew_price = reg_origin
    except:
        reg_origin = mark_origin.contents[2].span.string.strip().replace('.', '')
        reg_promotion = reg_origin
        renew_price = reg_origin
    return [reg_origin, reg_promotion, renew_price]


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
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='ESC'), domain_type='vn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_comvn():
            lst = get_comvn()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='ESC'), domain_type='comvn', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3]})
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='ESC'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='ESC'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='ESC'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='ESC'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2]})
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

        
    

        