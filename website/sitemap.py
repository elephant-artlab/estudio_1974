from django.contrib import sitemaps
from django.core.urlresolvers import reverse

class Sitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def __init__(self, names):
        self.names = names

    def items(self):
        items = (
                reverse('index'),
                reverse('realstate'),
                reverse('products-all'),
                reverse('products-new'),
                reverse('promotions'),
                reverse('highlight'),
                reverse('cart-list'),
                reverse('contact'),
            )
        return items

    def location(self, obj):
        return obj