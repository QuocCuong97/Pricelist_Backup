from django.contrib import admin
# from .models import SSL, Comodo
# # Register your models here.

# class SSLAdmin(admin.ModelAdmin):
#     list_display = ['vendor', 'ssl_type']
#     list_filter = ['vendor', 'ssl_type']
#     search_fields = ['vendor', 'ssl_type']
#     fieldsets = [
#         ('Tên nhà cung cấp', {'fields': ['vendor']}),
#         ('Loại SSL', {'fields': ['ssl_type']}),
#     ]
# class ComodoAdmin(admin.ModelAdmin):
#     list_display = ['vendor', 'ssl_type', 'price', 'validation_type', 'trust_level', 'support']
#     list_filter = ['vendor', 'ssl_type']
#     search_fields = ['vendor', 'ssl_type']
#     fieldsets = [
#         ('Tên nhà cung cấp', {'fields': ['vendor']}),
#         ('Loại SSL', {'fields': ['ssl_type']}),
#         ('Giá', {'fields': ['price']}),
#         ('Chứng thực', {'fields': ['validation_type']}),
#         ('Hỗ trợ SAN', {'fields': ['sans_support']}),
#         ('Số domain được bảo mật', {'fields': ['domain_secured']}),
#         ('Chính sách bảo hiểm', {'fields': ['warranty']}),
#         ('Mức độ tin cậy', {'fields': ['trust_level']}),
#         ('Thời hạn đăng ký', {'fields': ['validity_options']}),
#         ('Hỗ trợ 24/7', {'fields': ['support']}),
#     ]

# admin.site.register(SSL, SSLAdmin)
# admin.site.register(Comodo,ComodoAdmin)