# Create your views here.

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from django.shortcuts import render_to_response


from clinica.models import Patient, Staff, LabTest, Item, Visit


class PatientListView(ListView):
    model = Patient
    context_object_name = "patients"
    template_name = 'clinica/list_patient.html'


class StaffListView(ListView):
    pass


class LabTestView(ListView):
    pass


class ItemListView(ListView):
    pass


class VisitListView(ListView):
    pass


class CreatePatientView(CreateView):
    model = Patient
    template_name = 'clinica/add_patient.html'

    def get_success_url(self):
        pass

    '''@method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CreatePatientView,self).dispatch(*args,**kwargs)'''


class CreateStaffView(CreateView):
    model = Staff
    template_name = 'clinica/add_staff.html'


class CreateItemView(CreateView):
    model = Item
    template_name = 'clinica/add_item.html'


class CreateLabTestView(CreateView):
    model = LabTest
    template_name = 'clinica/add_lab_test.html'

class CreateVisitView(CreateView):
    pass


class UpdatePatientView(UpdateView):
    model = Patient
    template_name = 'clinica/add_patient.html'


class UpdateStaffView(UpdateView):
    model = Staff
    template_name = 'clinica/add_staff.html'

