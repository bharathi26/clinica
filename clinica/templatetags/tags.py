__author__ = 'julius'

from django import template
from clinica.models import Patient, Visit, Staff

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})

@register.inclusion_tag('visits.html')
def display_visits(patient_id):
    patient = Patient.objects.get(id__exact=patient_id)
    visits = Visit.objects.filter(patient_id=patient)[0:20]
    return {'visits': visits}


