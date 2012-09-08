from django.conf.urls import patterns, include, url
from creeply import views as c
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', c.home, name='home'),
    url(r'^linkedin/login/?$', c.lilogin, name='lilogin'),
    url(r'^facebook/login/?$', c.fblogin, name='fblogin'),
    url(r'^facebook/', include('django_facebook.urls')),
    url(r'^accounts/', include('django_facebook.auth_urls')),
    # Examples:
    # url(r'^hobby/', include('hobby.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
