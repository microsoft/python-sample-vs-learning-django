"""
Definition of urls for BasicProject.
"""

from django.conf.urls import include, url
import HelloDjangoApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),

    # Added with tutorial step 3-3
    url(r'^about$', HelloDjangoApp.views.about, name='about'),

    # Examples:
    # url(r'^$', BasicProject.views.home, name='home'),
    # url(r'^BasicProject/', include('BasicProject.BasicProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
