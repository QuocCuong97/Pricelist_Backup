import os

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from home.models import Domain, Vendor


class Command(BaseCommand):
    help = 'Crawl PriceList'

    def add_arguments(self, parser):
        parser.add_argument('-domain',action='store_true', help='sort_domain')
        parser.add_argument('-hosting',action='store_true', help='sort_hosting')
        parser.add_argument('-vps',action='store_true', help='vps')

    def handle(self, *args, **kwargs):
        if kwargs['domain']:
            lst_vn = Domain.objects.all().filter(domain_type='vn').order_by('sale_price').values('sale_price')
            lst_comvn = Domain.objects.all().filter(domain_type='comvn').order_by('sale_price').values_list('sale_price')
            lst_com = Domain.objects.all().filter(domain_type='com').order_by('sale_price').values_list('sale_price')
            lst_net = Domain.objects.all().filter(domain_type='net').order_by('sale_price').values_list('sale_price')
            lst_org = Domain.objects.all().filter(domain_type='org').order_by('sale_price').values_list('sale_price')
            lst_info = Domain.objects.all().filter(domain_type='info').order_by('sale_price').values_list('sale_price')
            lst_cheapest = [lst_com[0], lst_net[0], lst_org[0], lst_info[0], lst_comvn[0], lst_vn[0]]
            lst_second = [lst_com[1], lst_net[1], lst_org[1], lst_info[1], lst_comvn[1], lst_vn[1]]
            lst_third = [lst_com[2], lst_net[2], lst_org[2], lst_info[2], lst_comvn[2], lst_vn[2]]
            print(lst_cheapest)
            print(lst_second)
            print(lst_third)
        elif kwargs['hosting']:
            print('OK')
        elif kwargs['vps']:
            print('OK')
        else:
            print("Invalid options! Please type '-h' for help")
