from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class StaticSitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        items = (
                reverse('index'),
                reverse('home'),
                reverse('about'),
                reverse('sessions'),
                reverse('contact'),
            )
        return items

    def location(self, obj):
        return obj