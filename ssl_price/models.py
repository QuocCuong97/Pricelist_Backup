from django.db import models
from domain_price.models import Vendor
# Create your models here.

# class SSL(models.Model):
#     vendor = models.ManyToManyField(Vendor, through='Comodo')
#     ssl_type_choices = [
#         ('comodo', 'Comodo SSL'),
#         ('geotrust', 'GeoTrust SSL'),
#         ('symantec', 'Symantec SSL'),
#         ('thawte', 'Thawte SSL'),
#         ('globalsign', 'GlobalSign SSL')
#     ]
#     ssl_type = models.CharField(
#         max_length= 10,
#         choices = ssl_type_choices,
#         default = 'comodo',
#     )
#     def __str__(self):
#         return self.vendor.name + ' ' + self.ssl_type

# class Comodo(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     ssl_type = models.ForeignKey(SSL, on_delete=models.CASCADE)
#     pack_choices = [
#         ('pack_1', 'Positive SSL'),
#         ('pack_2', 'Positive SSL Multi Domain'),
#         ('pack_3', 'Positive SSL Wildcard'),
#         ('pack_4', 'Comodo EV SSL'),
#         ('pack_5', 'Premium SSL Wildcard'),
#         ('pack_6', 'Comodo EV Multi Domain SSL'),
#     ]
#     pack = models.CharField(
#         max_length=60,
#         choices=pack_choices,
#     )
#     price = models.DecimalField(max_digits = 8, decimal_places = 3, default='0')
#     validation_type_choices = [
#         ('DV', 'Domain Validation (DV)'),
#         ('EV', 'Extended Validation (EV)'),
#         ('OV', 'Organization Validation (OV)'),
#     ]
#     validation_type = models.CharField(
#         max_length=30,
#         choices=validation_type_choices,
#         default='DV',
#     )
#     sans_support = models.CharField(max_length=60, null=True)
#     domain_secured = models.CharField(max_length=40, null=True)
#     warranty = models.CharField(max_length=15, null=True)
#     trust_level_choices = [
#         ('standard', 'Standard'),
#         ('high', 'High'),
#         ('highest', 'Highest'),
#         ('unknown', 'Unknown'),
#     ]
#     trust_level = models.CharField(
#         max_length=10,
#         choices=trust_level_choices,
#         default='standard',
        
#     )
#     validity_options = models.CharField(max_length=15, null=True)
#     support = models.BooleanField(default='True')

    