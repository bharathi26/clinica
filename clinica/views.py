# Create your views here.

from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from clinica.models import Patient,Staff,LabTest,Item,Visit

class CreatePatientView(CreateView):
    model = Patient
    template_name = 'clinica/add_patient.html'

    def get_success_url(self):
        pass

class CreateStaffView(CreateView):
    model = Staff
    template_name = 'clinica/add_staff.html'

class CreateItemView(CreateView):
    model = Item
    template_name = 'clinica/add_item.html'

class CreateLabTestView(CreateView):
    model = LabTest
    template_name = 'clinica/add_lab_test.html'