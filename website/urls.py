# coding: utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('website.views',
	url(r'^$', 'home_view'),
	url(r'^home', 'home_view'),
	url(r'^about', 'about_view'),
	url(r'^sessions', 'sessions_view'),
	url(r'^contact', 'contact_view'),
)