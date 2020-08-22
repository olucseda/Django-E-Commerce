from django.contrib import admin

# Register your models here.
from siparis.models import ShopCart, Siparis, SiparisProduct
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter =  ['user']

class SiparisProductline(admin.TabularInline):
    model = SiparisProduct
    readonly_fields = ('user', 'product','price','quantity','amount')
    can_delete = False
    extra = 0


class SiparisAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','ip', 'last_name','phone','city','total')
    can_delete = False
    inlines = [SiparisProductline]

class SiparisProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','price','quantity','amount']
    list_filter = ['user']
    
admin.site.register(ShopCart,ShopCartAdmin)

admin.site.register(Siparis,SiparisAdmin)
admin.site.register(SiparisProduct,SiparisProductAdmin)