import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Vendor
from vps.models import VPS

homepage = "https://hostingviet.vn/"
urls_1 = "https://hostingviet.vn/vps-starter-gia-re"
urls_2 = "https://hostingviet.vn/vps-chuyen-nghiep"
urls_3 = "https://hostingviet.vn/vps-cao-cap"
source = "HostingViet"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom


def get_pack_1():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[0]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_3, price_6, price_12, urls_1]

def get_pack_2():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[1]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_3, price_6, price_12, urls_1]

def get_pack_3():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[2]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][10:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_1]

def get_pack_4():
    dom = get_dom(urls_1)
    mark = dom.findAll(class_="product-item")[3]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[3].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[7].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[5].string.strip('GB (Ram Swap tự điều chỉnh):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][10:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][10:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][10:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[10:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_1]

def get_pack_5():
    dom = get_dom(urls_2)
    mark = dom.findAll(class_="product-item")[0]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][22:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][22:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][22:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_2]

def get_pack_6():
    dom = get_dom(urls_2)
    mark = dom.findAll(class_="product-item")[1]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip()
    price_1 = int(mark.contents[5].contents[0].contents[0][22:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][22:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][22:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_2]

def get_pack_7():
    dom = get_dom(urls_2)
    mark = dom.findAll(class_="product-item")[2]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][22:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][22:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][22:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_2]

def get_pack_8():
    dom = get_dom(urls_3)
    mark = dom.findAll(class_="product-item")[0]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][23:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][23:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][23:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_3]

def get_pack_9():
    dom = get_dom(urls_3)
    mark = dom.findAll(class_="product-item")[1]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][23:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][23:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][23:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_3]

def get_pack_10():
    dom = get_dom(urls_3)
    mark = dom.findAll(class_="product-item")[2]
    pack = mark.contents[1].contents[0].string.upper()
    vcpu = mark.contents[3].contents[1].string.strip('CPU: v0').strip()
    ssd = mark.contents[3].contents[5].string.strip('Dung lượng lưu trữ SSD: GB')
    ram = mark.contents[3].contents[3].string.strip('GB (Không bao gồm Ram Swap):').strip().replace('GB', '')
    price_1 = int(mark.contents[5].contents[0].contents[0][23:].strip(' đ/tháng').replace('.', '')) * 1
    price_3 = int(mark.contents[5].contents[0].contents[2][23:].strip(' đ/tháng').replace('.', '')) * 3
    price_6 = int(mark.contents[5].contents[0].contents[4][23:].strip(' đ/tháng').replace('.', '')) * 6
    price_12 = int(mark.contents[5].contents[0].contents[6].text[22:].strip(' đ/tháng').replace('.', '')) * 12
    return [pack, vcpu, ssd, ram, price_1, price_3, price_6, price_12, urls_3]