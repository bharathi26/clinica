from django.db import models

# Create your models here.


class LabTest(models.Model):
    type = models.CharField(max_length=100, verbose_name="name")
    unit_cost = models.PositiveIntegerField(default=0, verbose_name='Unit Cost')

    def __unicode__(self):
        return u'%s' % self.type

    class Meta:
        verbose_name_plural = 'Lab Tests'
        ordering = ['type']


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name="Drug Name")
    quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")
    unit_cost = models.PositiveIntegerField(default=0, verbose_name="Retail Price")
    cost_price = models.PositiveIntegerField(default=0, verbose_name="Wholesale Price")

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Prescription Drugs'
        ordering = ['name']


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    address = models.CharField(max_length=100, verbose_name='address')
    phone = models.CharField(max_length=30, verbose_name='Phone Number')
    alternate_phone = models.CharField(max_length=30, verbose_name='Alternate Phone Number', blank=True)
    email = models.EmailField(max_length=100, verbose_name='Email', blank=True)

    def __unicode__(self):

        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Suppliers'
        ordering = ['name']


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='First Name')

    def __unicode__(self):

        return '%s  %s ' % self.name


class Debtor(models.Model):
    debt_date = models.DateField(auto_now_add=True, verbose_name='date')
    customer = models.CharField(max_length=100,verbose_name='customer')
    bill = models.PositiveIntegerField(verbose_name='bill')
    paid = models.PositiveIntegerField(verbose_name='Amount Paid')
    balance = models.PositiveIntegerField(verbose_name='balance')

    class Meta:
        verbose_name_plural = 'Debtors'

    def save(self, *args, **kwargs):

        #calculate balance before saving a debtor into the database

        self.balance = self.bill - self.paid

        super(Debtor, self).save(*args, **kwargs)


class Sale(models.Model):
    customer = models.CharField(max_length=100, blank=True, null=True, verbose_name='Customer Name(Optional)')
    processed_by = models.ForeignKey('clinica.Staff', verbose_name='Processed By')
    lab_tests = models.ManyToManyField(LabTest, through='SaleTest', verbose_name='Lab Tests', blank=True, null=True)
    drugs = models.ManyToManyField(Item, through='SaleItem', verbose_name='Drugs',blank=True, null=True)
    total_amount = models.PositiveIntegerField(verbose_name='Bill')
    full_pay = models.BooleanField(default=True, verbose_name='Full Payment', help_text='Please Uncheck if not full payment and enter customer name to keep track of debt')
    #payment = models.PositiveIntegerField(blank=True, verbose_name='Amount Paid', help_text='Input amount paid if its not full payment')

    def save(self, *args, **kwargs):

        lab_total = 0

        drug_total = 0

        #Calculate total quantity and amounts in receipted items

        for item in self.saletest_set.all():
            lab_total += item.test.unit_cost

        for item in self.drugs.all():

            drug_total += item.drug_amount

        self.total_amount = lab_total + drug_total

        '''if self.full_pay:
            self.payment = self.total_amount

        else:
            # we have a debtor entered into the system

            debtor = Debtor.objects.create(customer=self.customer, bill=self.total_amount, paid=self.payment)

            debtor.save()'''

        super(Sale, self).save(*args, **kwargs)

    def lab_test_names(self):
        '''return names of lab tests for each sale '''

        return ', '.join([a.type for a in self.lab_tests.all()])

    def prescription_names(self):
        """return prescriptions for a given sale"""

        return ','.join([a.name for a in self.drugs.all()])

    lab_test_names.short_description = 'Lab Tests'
    prescription_names.short_description = 'Prescriptions'


class SaleTest(models.Model):
    test = models.ForeignKey(LabTest)
    sale = models.ForeignKey(Sale)

    class Meta:
        verbose_name ='Lab Tests'
        verbose_name_plural = 'Lab Tests Taken'


class SaleItem(models.Model):
    item = models.ForeignKey(Item)
    sale = models.ForeignKey(Sale)
    quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")
    drug_amount = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'prescription'
        verbose_name_plural = 'Purchased Drug Items'

    '''def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        super(SaleItem, self).save(False, False, None,None)

        #self.drug_amount = self.item.unit_cost * self.quantity

        #update quantity field in Parent Model item

        self.item.quantity -= self.quantity

        self.item.save()

        if self.pk:
            self.drug_amount = self.item.unit_cost * self.quantity

        self.sale.save()'''












