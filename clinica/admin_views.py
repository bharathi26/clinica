from .models import Patient,Visit
from django.shortcuts import render_to_response
from django.template import RequestContext


def visits(request, pk):
    """ view that returns a list of visits made in the name of a particular patient """

    return render_to_response(
        "admin/clinica/visits.html",
        {'visit_list': Visit.objects.filter(patient_id=pk)},
        RequestContext(request, {}),
    )


def assignments(request, pk):

    """
    :param request: view returns visits assigned to a particular staff member
    :param pk:
    :return:
    """

    return render_to_response(
        "admin/clinica/assigments.html",
        {'visit_list': Visit.objects.filter(attendant=pk)},
        RequestContext(request, {}),
    )





