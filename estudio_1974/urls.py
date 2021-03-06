from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from website.sitemap import StaticSitemap

admin.autodiscover()

sitemaps = {
'sitemap': StaticSitemap,
}

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('website.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
	)