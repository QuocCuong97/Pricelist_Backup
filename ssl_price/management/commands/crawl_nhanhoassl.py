import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from domain_price.models import Vendor
from ssl_price.models import SSL

homepage = "https://nhanhoa.com/"
source = "NhanHoa"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_comodo():
    dom = get_dom('https://nhanhoa.com/ssl-bao-mat/bang-gia-comodo-ssl.html')
    