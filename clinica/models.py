from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
)

STAFF_DESIGNATION = (
    ('Doctor','Doctor'),
    ('Nurse','Nurse'),
    ('Lab Technician','Laboratory Technician'),
    ('Receptionist','Receptionist'),
)

CLINIC_TYPE = (
    ('IN','INPATIENT'),
    ('OUT','OUTPATIENT'),
)

class Patient(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='First Name')
    last_name = models.CharField(max_length=30,verbose_name='Last Name')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,verbose_name='Gender')
    address = models.CharField(max_length=100,blank=True,verbose_name='Address')
    phone  = models.CharField(max_length=30,blank=True,verbose_name='Phone')
    dob = models.CharField(max_length=30,verbose_name='Date of Birth',help_text='Please enter date of birth in format:dd/mm/yy',blank=True)
    age = models.PositiveSmallIntegerField(default=0,blank=False,verbose_name='Age')

    def __unicode__(self):

        return self.first_name + self.last_name

    def _get_full_name(self):
        "returns the person's full name"

        return '%s %s' % (self.first_name,self.last_name)

    full_name = property(_get_full_name)

class Staff(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='First Name')
    last_name = models.CharField(max_length=30,verbose_name='Last Name')
    phone = models.CharField(max_length=30,verbose_name='Phone')
    alternate_phone = models.CharField(max_length=30,blank=True,verbose_name='Alternate Phone')
    email = models.EmailField(blank=True,verbose_name='Email')
    designation = models.CharField(max_length=50,choices=STAFF_DESIGNATION,verbose_name='Designation')

    def __unicode__(self):

        return self.first_name + self.last_name


class LabTest(models.Model):
    type = models.CharField(max_length=100,verbose_name="Name")
    unit_cost = models.PositiveIntegerField(default=0,verbose_name='Unit Cost')

    def __unicode__(self):
        return self.type

class Item(models.Model):
    name = models.CharField(max_length=100,verbose_name="Drug Name")
    quantity = models.PositiveIntegerField(default=0,verbose_name="Quantity")
    unit_cost = models.PositiveIntegerField(default=0,verbose_name="Retail Price")
    cost_price = models.PositiveIntegerField(default=0,verbose_name="Wholesale Price")

    def __unicode__(self):
        return self.name

class PrescriptionItem(models.Model):
    name_id = models.ForeignKey(Item)
    dosage_qty = models.PositiveIntegerField(default=0,verbose_name="Dosage Quantity")

    def __unicode__(self):
        return self.name_id.name

class Visit(models.Model):
    patient_id = models.ForeignKey(Patient,verbose_name="Patient")
    category = models.CharField(max_length=10,choices=CLINIC_TYPE,verbose_name="Type of Visit")
    diagnosis = models.TextField(verbose_name="Diagnosis")
    attendant = models.ForeignKey(Staff,verbose_name='Attended to by')
    consultation = models.BooleanField(default='True',verbose_name="Consultation with Doctor Needed?")
    visit_date = models.DateTimeField(auto_now_add=True,verbose_name="Visit Date")
    lab_tests = models.ManyToManyField(LabTest,verbose_name='Required Lab Tests')
    prescriptions = models.ManyToManyField(PrescriptionItem,verbose_name='Prescriptions')




