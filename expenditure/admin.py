__author__ = 'julius'

from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('particulars', 'amount', 'incurred_by', 'expense_date')


admin.site.register(Expense, ExpenseAdmin)



