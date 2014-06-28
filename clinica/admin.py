__author__ = 'julius kimuli'

from django.contrib import admin
from clinica.models import Patient,Staff

class PatientAdmin(admin.ModelAdmin):
    pass

class StaffAdmin(admin.ModelAdmin):
    pass


admin.site.register(Staff,StaffAdmin)
admin.site.register(Patient,PatientAdmin)