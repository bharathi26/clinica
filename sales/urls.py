__author__ = 'julius'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from sales import views

urlpatterns = patterns(' ',

    url(r'item/$', views.ItemListView.as_view(), name='item-list'),
    url(r'^test/$', views.LabTestListView.as_view(), name='test-list'),

    url(r'^item/new/$', login_required(views.CreateItemView.as_view()), name='item-new'),
    url(r'^test/new/$', login_required(views.CreateLabTestView.as_view()), name='test-new'),

    url(r'^item/edit/(?P<pk>[0-9]+)/$', login_required(views.UpdateItemView.as_view()),name='item-edit'),
    url(r'^test/edit/(?P<pk>[0-9]+)/$', login_required(views.UpdateLabTestView.as_view()),name='test-edit'),

    #url(r'^sale/$', views.SaleListView.as_view(),name='sale-list'),
    url(r'^sale/new/$', views.CreateSaleInline.as_view(), name='sale-new'),

)
