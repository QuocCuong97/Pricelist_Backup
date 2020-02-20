from django.contrib import admin
from .models import Domain, Vendor
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'homepage']
    list_filter = ['name']
    search_fields = ['name']
    fieldsets = [
        ('Tên nhà cung cấp', {'fields': ['name']}),
        ('Trang chủ', {'fields': ['homepage']}),
        ('Logo', {'fields': ['logo']})
    ]

class DomainAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'domain_type', 'reg_origin', 'reg_promotion', 'renew_price', 'trans_price']
    list_filter = ['domain_type', 'vendor']
    search_fields = ['domain_type']
    fieldsets = [
        ('Nhà cung cấp', {'fields': ['vendor']}),
        ('Loại tên miền', {'fields': ['domain_type']}),
        ('Giá gốc đăng ký năm đầu', {'fields': ['reg_origin']}),
        ('Giá khuyến mãi đăng ký năm đầu', {'fields': ['reg_promotion']}),
        ('Phí duy trì', {'fields': ['renew_price']}),
        ('Phí transfer', {'fields': ['trans_price']}),
    ]

# class HostingAdmin(admin.ModelAdmin):
#     list_display = ['vendor', 'price', 'quotes', 'bandwidths']
#     fieldsets = [
#         ('Nhà cung cấp', {'fields': ['vendor']}),
#         ('Giá', {'fields': ['price']}),
#         ('Dung lượng đám mây', {'fields': ['quotes']}),
#         ('Băng thông', {'fields': ['bandwidths']}),
#     ]

# class VPSAdmin(admin.ModelAdmin):
#     list_display = ['vendor', 'price', 'cpu', 'disk', 'ram']
#     fieldsets = [
#         ('Nhà cung cấp', {'fields': ['vendor']}),
#         ('Giá', {'fields': ['price']}),
#         ('CPU', {'fields': ['cpu']}),
#         ('SSD/HDD', {'fields': ['disk']}),
#         ('RAM', {'fields': ['ram']}),
#     ]

admin.site.register(Domain, DomainAdmin)
admin.site.register(Vendor, VendorAdmin)
# admin.site.register(Hosting, HostingAdmin)
# admin.site.register(VPS, VPSAdmin)

admin.site.site_header = "Trang quản trị Website"