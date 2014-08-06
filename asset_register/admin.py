from django.contrib import admin
from .models import Asset

# Register your models here.


class FixedAssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'acquired_on', 'service_period', 'last_service_date', 'service_due')
    list_filter = ('category',)


admin.site.register(Asset,FixedAssetAdmin)