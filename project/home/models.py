from django.db import models

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=20, unique=True)
    homepage = models.TextField()

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
    origin_price = models.CharField(max_length=20, default="0")
    sale_price = models.CharField(max_length=20, default="0")
    def __str__(self):
        return self.vendor.name + ' ' + self.domain_type

class Hosting(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.CharField(max_length=20, default="0")
    quotes = models.CharField(max_length=20, default="0")
    bandwidths = models.CharField(max_length=20, default="0")
    def __str__(self):
        return self.vendor.name + 'Hosting'


class VPS(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.CharField(max_length=20, default="0")
    cpu = models.CharField(max_length=40, default="0")
    disk = models.CharField(max_length=20, default="0")
    ram = models.CharField(max_length=20, default="0")
    def __str__(self):
        return self.vendor.name + 'VPS'