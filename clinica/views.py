# Create your views here.

from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from django.views.generic import ListView

from clinica.models import Patient, Staff, Visit


class PatientListView(ListView):
    model = Patient
    context_object_name = "patients"
    template_name = 'clinica/list_patient.html'


class StaffListView(ListView):
    model = Staff
    context_object_name = "staff"
    template_name = "clinica/list_staff.html"


class VisitListView(ListView):
    model = Visit
    context_object_name = "visits"
    template_name = "clinica/list_visit.html"


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


class CreateVisitView(CreateView):
    model = Visit
    template_name = 'clinica/add_visit.html'


class UpdatePatientView(UpdateView):
    model = Patient
    template_name = 'clinica/add_patient.html'


class UpdateStaffView(UpdateView):
    model = Staff
    template_name = 'clinica/add_staff.html'


class UpdateVisitView(UpdateView):
    pass





