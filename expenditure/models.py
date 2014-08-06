from django.db import models

# Create your models here.


class Expense(models.Model):
    expense_date = models.DateField(auto_now_add=True, verbose_name="Date Expense Incurred")
    particulars = models.TextField(verbose_name='Particulars')
    amount = models.PositiveIntegerField(verbose_name='Amount')
    incurred_by = models.ForeignKey('clinica.Staff')

    def __unicode__(self):

        return '%s - %d incurred by %s' % (self.particulars, self.amount, self.incurred_by)

    class Meta:
        verbose_name_plural = 'Expenses'
