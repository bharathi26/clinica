__author__ = 'julius'

from django.conf.urls import patterns,url
from clinica import views

urlpatterns = patterns('',

    url(r'^add_patient/$', views.CreatePatientView.as_view(),name='patient-new'),
    url(r'^add_staff/$',views.CreateStaffView.as_view(),name='staff-new'),

)
