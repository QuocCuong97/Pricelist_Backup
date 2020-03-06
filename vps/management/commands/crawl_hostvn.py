import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Vendor
from vps.models import VPS

homepage = "https://hostvn.net/"
urls = "https://hostvn.net/cloud/cloud-vps/"
source = "HostVN"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_pack_512():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[0]
    pack = mark.h3.contents[1].string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text
    if ram.find('MB') == -1:
        ram = ram.strip('GB')
    else:
        ram = str(float(ram.strip(' MB')) / 1024)
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_1():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[1]
    pack = mark.contents[1].h3.string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text.strip(' GB')
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_2():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[2]
    pack = mark.contents[1].h3.string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text.strip(' GB')
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_4():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[3]
    pack = mark.contents[1].h3.string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text.strip(' GB')
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_6():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[4]
    pack = mark.contents[1].h3.string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text.strip(' GB')
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_8():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[5]
    pack = mark.contents[1].h3.string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text.strip(' GB')
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_12():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[6]
    pack = mark.contents[1].h3.string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text.strip(' GB')
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]

def get_pack_16():
    dom = get_dom(urls)
    mark = dom.findAll(class_="package-2 flex-box")[7]
    pack = mark.contents[1].h3.string
    vcpu = mark.contents[3].contents[1].contents[1].contents[2].text.strip()
    ssd = mark.contents[3].contents[1].contents[5].contents[2].text.strip(' GB')
    ram = mark.contents[3].contents[1].contents[3].contents[2].text.strip(' GB')
    price_1 = mark.contents[5].contents[1].contents[1].string[11:].strip('đ').replace('.', '')
    price_3 = mark.contents[5].contents[1].contents[2].string[11:].strip('đ').replace('.', '')
    price_6 = mark.contents[5].contents[1].contents[3].string[11:].strip('đ').replace('.', '')
    price_12 = mark.contents[5].contents[1].contents[4].string[11:].strip('đ').replace('.', '')
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls]