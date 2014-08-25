__author__ = 'julius'

from django.contrib import admin
from .models import Item, LabTest, Supplier, Sale, SaleItem,SaleTest,Debtor


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
    exclude = ('drug_amount',)

    def save_model(self, request, obj, form, change):

        obj.drug_amount = obj.item.unit_cost * form.cleaned_data['quantity']

        super(SaleItemAdmin, self).save_model(request, obj, form, change)


class SaleTestAdmin(admin.TabularInline):
    model = SaleTest


class SaleAdmin(admin.ModelAdmin):
    exclude = ('total_amount',)
    list_display = ('customer', 'processed_by', 'total_amount', 'full_pay', 'lab_test_names', 'prescription_names')
    inlines = [SaleItemAdmin, SaleTestAdmin]


admin.site.register(Sale, SaleAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(LabTest, TestAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Debtor)