__author__ = 'julius'

from django.conf.urls import patterns,url
from django.contrib.auth.decorators import login_required
from clinica import views

urlpatterns = patterns('',


    url(r'^patient/$', views.PatientListView.as_view(),name='patient-list'),
    url(r'^staff/$',views.StaffListView.as_view(),name='staff-list'),
    url(r'^item/$',views.ItemListView.as_view(),name='item-list'),
    url(r'^test/$',views.LabTestListView.as_view(),name='test-list'),
    url(r'^visit/$',views.VisitListView.as_view(),name='visit-list'),

    url(r'^patient/new/$', login_required(views.CreatePatientView.as_view()),name='patient-new'),
    url(r'^staff/new/$', login_required(views.CreateStaffView.as_view()),name='staff-new'),
    url(r'^item/new/$', views.CreateItemView.as_view(),name='item-new'),
    url(r'^test/new/$', views.CreateLabTestView.as_view(),name='test-new'),
    url(r'^visit/new/$',views.CreateVisitView.as_view(),name='visit-new'),


    #Url patterns for editing model entities

    url(r'^patient/edit/(?P<pk>[0-9]+)/$', views.UpdatePatientView.as_view(),name='patient-edit'),
    url(r'^staff/edit/(?P<pk>[0-9]+)/$', views.UpdateStaffView.as_view(),name='staff-edit'),
    url(r'^item/edit/(?P<pk>[0-9]+)/$',views.UpdateItemView.as_view(),name='item-edit'),
    url(r'^test/edit/(?P<pk>[0-9]+/$',views.UpdateLabTestView.as_view(),name='test-edit'),
    url(r'^visit/edit/(?P<pk>[0-9]+/$',views.UpdateVisitView.as_view(),name='visit-edit'),
)
