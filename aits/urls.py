from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aits.views.home', name='home'),
    # url(r'^aits/', include('aits.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^admin/patient/(?P<pk>[0-9]+)/visits/$', 'clinica.admin_views.visits'),

    url(r'^admin/staff/(?P<pk>[0-9]+)/visits/$', 'clinica.admin_views.assignments'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login'}),
    url(r'^clinica/', include('clinica.urls')),
    url(r'^sales/', include('sales.urls')),

    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
)

urlpatterns += staticfiles_urlpatterns()
