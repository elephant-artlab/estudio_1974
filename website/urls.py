# coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
	url(r'^$', 'about_view', name='index'),
	url(r'^home', 'home_view', name='home'),
	url(r'^about', 'about_view', name='about'),
	url(r'^sessions', 'sessions_view', name='sessions'),
	url(r'^contact', 'contact_view', name='contact'),
)