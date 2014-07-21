from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

STAFF_DESIGNATION = (
    ('Doctor', 'Doctor'),
    ('Nurse', 'Nurse'),
    ('Lab Technician', 'Laboratory Technician'),
    ('Receptionist', 'Receptionist'),
)

CLINIC_TYPE = (
    ('IN', 'INPATIENT'),
    ('OUT', 'OUTPATIENT'),
)


class Patient(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name='gender')
    address = models.CharField(max_length=100,blank=True,verbose_name='address')
    phone = models.CharField(max_length=30,blank=True, verbose_name='phone')
    dob = models.CharField(max_length=30,verbose_name='Date of Birth', help_text='Please enter date of birth in format:dd/mm/yy', blank=True)
    age = models.PositiveSmallIntegerField(default=0,verbose_name='age')

    class Meta:
        verbose_name_plural = 'Patients'
        ordering = ['first_name']

    def __unicode__(self):

        return u'%s %s' % (self.first_name, self.last_name)

    def _get_full_name(self):
        """returns the person's full name"""

        return '%s  %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)


class Staff(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='First Name')
    last_name = models.CharField(max_length=30,verbose_name='Last Name')
    phone = models.CharField(max_length=30,verbose_name='phone')
    alternate_phone = models.CharField(max_length=30,blank=True,verbose_name='Alternate Phone')
    email = models.EmailField(blank=True,verbose_name='email')
    designation = models.CharField(max_length=50,choices=STAFF_DESIGNATION,verbose_name='designation')

    class Meta:
        verbose_name_plural = 'Staff'
        ordering =['first_name']

    def __unicode__(self):

        return u'%s %s' % (self.first_name, self.last_name)

    def _get_full_name(self):
        """ returns the person's full name """

        return u'%s  %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)


class LabTest(models.Model):
    type = models.CharField(max_length=100, verbose_name="name")
    unit_cost = models.PositiveIntegerField(default=0, verbose_name='Unit Cost')

    def __unicode__(self):
        return u'%s' % self.type

    class Meta:
        verbose_name_plural = 'Lab Tests'
        ordering = ['type']


class Item(models.Model):
    name = models.CharField(max_length=100,verbose_name="Drug Name")
    quantity = models.PositiveIntegerField(default=0,verbose_name="quantity")
    unit_cost = models.PositiveIntegerField(default=0,verbose_name="Retail Price")
    cost_price = models.PositiveIntegerField(default=0,verbose_name="Wholesale Price")

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Prescription Drugs'
        ordering = ['name']


class Visit(models.Model):
    patient_id = models.ForeignKey(Patient, verbose_name="patient")
    category = models.CharField(max_length=10, choices=CLINIC_TYPE, verbose_name="Visit Type")
    diagnosis = models.TextField(verbose_name="diagnosis")
    attendant = models.ForeignKey(Staff, verbose_name='attendant')
    consultation = models.BooleanField(default='True', verbose_name="consultation")
    visit_date = models.DateTimeField(auto_now_add=True, verbose_name="Visit Date")
    lab_tests = models.ManyToManyField(LabTest, verbose_name=' Lab Tests', through='VisitTest')
    prescriptions = models.ManyToManyField(Item, verbose_name='Prescriptions',  through='VisitItem')

    class Meta:
        verbose_name_plural = 'Clinic Visits'

    def lab_test_names(self):
        '''return names of lab tests for each visit '''

        return ', '.join([a.type for a in self.lab_tests.all()])

    def prescription_names(self):
        """return prescriptions for a given visit"""

        return ','.join([a.name for a in self.prescriptions.all()])

    lab_test_names.short_description = 'Lab Tests'
    prescription_names.short_description = 'Prescriptions'

class VisitTest(models.Model):
    test = models.ForeignKey(LabTest)
    visit = models.ForeignKey(Visit)

    class Meta:

        verbose_name = 'lab test'
        verbose_name_plural = 'Lab Tests Taken'


class VisitItem(models.Model):
    item = models.ForeignKey(Item)
    visit = models.ForeignKey(Visit)
    quantity = models.PositiveIntegerField(default=0, verbose_name="quantity")

    class Meta:
        verbose_name = 'prescription'
        verbose_name_plural = 'Prescribed Drugs'





