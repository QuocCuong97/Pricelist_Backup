import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Crawl All of PriceList'
    

    def add_arguments(self, parser):
        parser.add_argument('-all',action='store_true', help='crawl all')

    def handle(self, *args, **kwargs):
        if kwargs['all']:
            os.system("python manage.py crawl_nhanhoa -a")
            os.system("python manage.py crawl_matbao -a")
            os.system("python manage.py crawl_pa -a")
            os.system("python manage.py crawl_bkns -a")
            os.system("python manage.py crawl_esc -a")
            os.system("python manage.py crawl_hostingviet -a")
            os.system("python manage.py crawl_hostvn -a")
            os.system("python manage.py crawl_tenten -a")
            os.system("python manage.py crawl_vhost -a")
            os.system("python manage.py crawl_inet -a")
            os.system("python manage.py crawl_bkhost -a")
            os.system("python manage.py crawl_godaddy -a")
            os.system("python manage.py crawl_viettel -a")
            os.system("python manage.py crawl_tnd -a")
            os.system("python manage.py crawl_vinahost -a")
            os.system("python manage.py crawl_zcom -a")
            os.system("python manage.py crawl_azdigi -a")
            os.system("python manage.py crawl_porkbun -a")
            os.system("python manage.py crawl_hostinger -a")
            
        else:
            print("Invalid options! Please type '-h' for help")