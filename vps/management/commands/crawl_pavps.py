import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Vendor
from vps.models import VPS

homepage = "https://www.pavietnam.vn/"
urls = "https://www.pavietnam.vn/vn/vps-server.html"
source = "P.A VietNam"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_pack_0():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[1]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(price_1) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 12)
    except:
        pass
    note = "Thuê từ 3 tháng trở lên"
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls, note]

def get_pack_1():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[3]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(price_1) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 6)
    price_12 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 12)
    note = "Thuê từ 3 tháng trở lên"
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls, note]

def get_pack_2():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[5]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_3():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[7]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_4():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[9]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_5():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[11]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_6():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[13]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_7():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[15]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_8():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[17]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_9():
    dom = get_dom(urls)
    mark = dom.find(class_="package server").contents[19]
    pack = mark.contents[1].contents[1].string.upper()
    vcpu = mark.contents[1].find(class_="row_item CORE").contents[3].string.strip(' cores')
    ssd = mark.contents[1].find(class_="row_item HDD").contents[3].string.strip(' GB[SSD Cloud Storage]')
    ram = mark.contents[1].find(class_="row_item RAM").contents[3].contents[0].strip(' +')
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip('MB')) / 1024)
    price_1 = mark.find(class_="list_plan").contents[1].contents[0].strip().replace('.', '')
    price_3 = str(int(mark.find(class_="list_plan").contents[3].contents[0].strip().replace('.', '')) * 3)
    price_6 = str(int(mark.find(class_="list_plan").contents[5].contents[0].strip().replace('.', '')) * 6)
    try:
        price_12 = str(int(mark.find(class_="list_plan").contents[7].contents[0].strip().replace('.', '')) * 12)
    except:
        price_12 = (int(mark.find(class_="price").contents[0].replace('.', '')) * 12)
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]



class Command(BaseCommand):
    help = 'Crawl PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-0',action='store_true', help='crawl pack 0')
        parser.add_argument('-1',action='store_true', help='crawl pack 1')
        parser.add_argument('-2',action='store_true', help='crawl pack 2')
        parser.add_argument('-3',action='store_true', help='crawl pack 3')
        parser.add_argument('-4',action='store_true', help='crawl pack 4')
        parser.add_argument('-5',action='store_true', help='crawl pack 5')
        parser.add_argument('-6',action='store_true', help='crawl pack 6')
        parser.add_argument('-7',action='store_true', help='crawl pack 7')
        parser.add_argument('-8',action='store_true', help='crawl pack 8')
        parser.add_argument('-9',action='store_true', help='crawl pack 9')
        parser.add_argument('-a',action='store_true', help='crawl all')
    

    def handle(self, *args, **kwargs):
        def new_pack_0():
            lst = get_pack_0()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8], 'note': lst[9]})
        def new_pack_1():
            lst = get_pack_1()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8], 'note': lst[9]})
        def new_pack_2():
            lst = get_pack_2()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_3():
            lst = get_pack_3()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_4():
            lst = get_pack_4()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_5():
            lst = get_pack_5()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_6():
            lst = get_pack_6()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_7():
            lst = get_pack_7()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_8():
            lst = get_pack_8()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        def new_pack_9():
            lst = get_pack_9()
            new_object = VPS.objects.update_or_create(vendor=Vendor.objects.get(name='P.A VietNam'), pack=lst[0], defaults = {'vcpu': lst[1], 'ssd': lst[2], 'ram': lst[3], 'price_1': lst[4], 'price_3': lst[5], 'price_6': lst[6], 'price_12': lst[7], 'link': lst[8]})
        if kwargs['0']:
            new_pack_0()
        elif kwargs['1']:
            new_pack_1()
        elif kwargs['2']:
            new_pack_2()
        elif kwargs['3']:
            new_pack_3()
        elif kwargs['4']:
            new_pack_4()
        elif kwargs['5']:
            new_pack_5()
        elif kwargs['6']:
            new_pack_6()
        elif kwargs['7']:
            new_pack_7()
        elif kwargs['8']:
            new_pack_8()
        elif kwargs['9']:
            new_pack_9()
        elif kwargs['a']:
            new_pack_0()
            new_pack_1()
            new_pack_2()
            new_pack_3()
            new_pack_4()
            new_pack_5()
            new_pack_6()
            new_pack_7()
            new_pack_8()
            new_pack_9()
        else:
            print("Invalid options! Please type '-h' for help")