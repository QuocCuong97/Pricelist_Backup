from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=20, unique=True)
    homepage = models.CharField(max_length=30, unique=True)
    vendor_location_choices = [
        ('FOR', 'Foreign'),
        ('VN', 'VietNam')
    ]
    vendor_location = models.CharField(
        max_length=10,
        choices=vendor_location_choices,
        default='VN',
    )
    logo = models.CharField(max_length=30, unique=True, null=True)
    def __str__(self):
        return self.name

class Domain(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    domain_type_choices = [
        ('vn', '.vn'),
        ('com', '.com'),
        ('comvn', '.com.vn'),
        ('net', '.net'),
        ('org', '.org'),
        ('info', '.info'),
    ]
    domain_type = models.CharField(
        max_length=10,
        choices=domain_type_choices,
        default='vn',
    )
    reg_origin = models.DecimalField(max_digits = 8, decimal_places = 3, null=True)
    reg_origin_usd = models.CharField(max_length=10, blank=True)
    reg_promotion = models.DecimalField(max_digits = 8, decimal_places = 3, null=True)
    reg_promotion_usd = models.CharField(max_length=10, blank=True)
    renew_price = models.DecimalField(max_digits = 8, decimal_places = 3, null=True)
    renew_price_usd = models.CharField(max_length=10, blank=True)
    trans_price = models.DecimalField(max_digits = 8, decimal_places = 3, null=True)
    trans_price_usd = models.CharField(max_length=10, blank=True)
    rates = models.CharField(max_length=10, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.vendor.name + ' ' + self.domain_type

# class Hosting(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     price = models.CharField(max_length=20, default="0")
#     quotes = models.CharField(max_length=20, default="0")
#     bandwidths = models.CharField(max_length=20, default="0")
#     def __str__(self):
#         return self.vendor.name + 'Hosting'


# class VPS(models.Model):
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
#     price = models.CharField(max_length=20, default="0")
#     cpu = models.CharField(max_length=40, null=True)
#     core = models.CharField(max_length=3, default="0")
#     disk = models.CharField(max_length=20, default="0")
#     ram = models.CharField(max_length=20, default="0")
#     def __str__(self):
#         return self.vendor.name + 'VPS'