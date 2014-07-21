__author__ = 'julius kimuli'

from django.contrib import admin
from django.contrib.sites.models import Site
from clinica.models import Patient, Staff, LabTest, Item, VisitTest, VisitItem, Visit


class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'alternate_phone', 'email', 'designation',)
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('designation',)


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
    list_display = ('first_name', 'last_name', 'phone', 'address', 'dob', 'age',)
    search_fields = ('first_name', 'last_name', 'address', 'phone', 'age')
    list_per_page = 50
    list_filter = ('address', 'age')

    def visits(self):
        return '<a href="?visit=%d">%s</a>' % (self.patient_id, self.patient)
    visits.allow_tags = True


admin.site.register(Staff, StaffAdmin)
admin.site.register(Patient, PatientAdmin)


admin.site.register(Item, ItemAdmin)
admin.site.register(LabTest, TestAdmin)
admin.site.register(Visit, VisitAdmin)

admin.site.unregister(Site)
