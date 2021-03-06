import json

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Domain, Vendor

homepage = "https://www.namebright.com/"
urls = "https://www.namebright.com/Pricing.aspx"
source = "NameBright"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_rate():
    page = requests.get("https://www.freeforexapi.com/api/live?pairs=USDVND").text
    dic = json.loads(page)
    return dic['rates']["USDVND"]['rate']

def get_com():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".com").parent
    reg_origin_usd = str(mark_reg.contents[5].contents[0].string.strip('$')) + str(mark_reg.contents[5].contents[2].string)
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = reg_origin_usd
    renew_price = reg_origin
    trans_price_usd = reg_origin_usd
    trans_price = reg_origin
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]

def get_net():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".net").parent
    reg_origin_usd = str(mark_reg.contents[5].contents[0].string.strip('$')) + str(mark_reg.contents[5].contents[2].string)
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = reg_origin_usd
    renew_price = reg_origin
    trans_price_usd = reg_origin_usd
    trans_price = reg_origin
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]

def get_org():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".org").parent
    reg_origin_usd = str(mark_reg.contents[5].contents[1].string.strip('$')) + str(mark_reg.contents[5].contents[3].string)
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = reg_origin_usd
    renew_price = reg_origin
    trans_price_usd = reg_origin_usd
    trans_price = reg_origin
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]

def get_info():
    dom_origin = get_dom(urls)
    mark_reg = dom_origin.find('td', text=".info").parent
    reg_origin_usd = str(mark_reg.contents[5].contents[1].string.strip('$')) + str(mark_reg.contents[5].contents[3].string)
    reg_origin = round(float(reg_origin_usd)  * get_rate())
    reg_promotion_usd = reg_origin_usd
    reg_promotion = reg_origin
    renew_price_usd = reg_origin_usd
    renew_price = reg_origin
    trans_price_usd = reg_origin_usd
    trans_price = reg_origin
    return [reg_origin, reg_promotion, renew_price, trans_price, reg_origin_usd, reg_promotion_usd, renew_price_usd, trans_price_usd]


class Command(BaseCommand):
    help = 'Crawl PriceList'


    def add_arguments(self, parser):
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-org',action='store_true', help='crawl .org')
        parser.add_argument('-info',action='store_true', help='crawl .info')
        parser.add_argument('-a',action='store_true', help='crawl all')


    def handle(self, *args, **kwargs):
        def new_com():
            lst = get_com()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NameBright'), domain_type='com', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
        def new_net():
            lst = get_net()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NameBright'), domain_type='net', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
        def new_org():
            lst = get_org()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NameBright'), domain_type='org', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
        def new_info():
            lst = get_info()
            new_object = Domain.objects.update_or_create(vendor=Vendor.objects.get(name='NameBright'), domain_type='info', defaults = {'reg_origin': lst[0], 'reg_promotion': lst[1], 'renew_price': lst[2], 'trans_price': lst[3], 'reg_origin_usd': lst[4], 'reg_promotion_usd': lst[5], 'renew_price_usd': lst[6], 'trans_price_usd': lst[7]})
        if kwargs['com']:
            new_com()
        elif kwargs['net']:
            new_net()
        elif kwargs['org']:
            new_org()
        elif kwargs['info']:
            new_info()
        elif kwargs['a']:
            new_com()
            new_net()
            new_org()
            new_info()
        else:
            print("Invalid options! Please type '-h' for help")