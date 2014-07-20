__author__ = 'julius'

from django.forms import ModelForm
from clinica.models import Staff,Patient,Visit

#create a ModelForm class for the Patient Model

class PatientForm(ModelForm):
    class Meta:
        model = Patient



class StaffForm(ModelForm):
    class Meta:
        model = Staff


class VisitForm(ModelForm):
    class Meta:
        model = Visit