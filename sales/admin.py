__author__ = 'julius'

from django.contrib import admin
from .models import Item, LabTest, Supplier, Sale, SaleItem,SaleTest


class TestAdmin(admin.ModelAdmin):
    list_display = ('type', 'unit_cost',)
    search_fields = ('type',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit_cost', 'cost_price',)
    search_fields = ('name',)


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address', 'phone', 'alternate_phone', 'email',)


class SaleItemAdmin(admin.TabularInline):
    model = SaleItem


class SaleTestAdmin(admin.TabularInline):
    model = SaleTest


class SaleAdmin(admin.ModelAdmin):
    exclude = ('total_amount',)
    inlines = [SaleItemAdmin, SaleTestAdmin]


admin.site.register(Sale, SaleAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(LabTest, TestAdmin)
admin.site.register(Supplier,SupplierAdmin)