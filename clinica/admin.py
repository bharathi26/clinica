__author__ = 'julius kimuli'

from django.contrib import admin
from django.contrib.sites.models import Site
from clinica.models import Patient, Staff, LabTest, Item, VisitTest, VisitItem, Visit, FixedAssetInventory,Supplier


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'address', 'phone', 'alternate_phone', 'email',)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'alternate_phone', 'email', 'designation', 'assignment',)
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('designation',)

    def assignment(self, request):

        return "<a href='/admin/staff/%d/visits'>Assignments</a>" % request.id

    assignment.allow_tags = True

class FixedAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'acquired_on', 'service_period', 'last_service_date', 'service_due')
    list_filter = ('category',)


class VisitItemInline(admin.TabularInline):
    model = VisitItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'unit_cost', 'cost_price',)
    search_fields = ('name',)


class VisitTestInline(admin.TabularInline):
    model = VisitTest


class TestAdmin(admin.ModelAdmin):
    list_display = ('type', 'unit_cost',)
    search_fields = ('type',)


class VisitAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'category', 'diagnosis', 'attendant', 'consultation', 'visit_date', 'lab_test_names','prescription_names')
    #date_hierarchy = 'visit_date'
    list_per_page = 50
    list_filter = ('patient_id', 'category', 'attendant', 'patient_id__gender', 'visit_date',)

    inlines = [VisitItemInline, VisitTestInline]


class VisitPatient(admin.TabularInline):
    model = Visit


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'address', 'dob', 'age', 'history')
    search_fields = ('first_name', 'last_name', 'address', 'phone', 'age')
    list_per_page = 50
    list_filter = ('address', 'age')

    def history(self, request):

        return "<a href='/admin/patient/%d/visits'>History</a>" % request.id

    history.allow_tags = True




admin.site.register(Staff, StaffAdmin)
admin.site.register(Patient, PatientAdmin)


admin.site.register(Item, ItemAdmin)
admin.site.register(LabTest, TestAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(FixedAssetInventory, FixedAssetAdmin)
admin.site.register(Supplier,SupplierAdmin)

admin.site.unregister(Site)
