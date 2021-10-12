from django.contrib.sitemaps import  Sitemap
from .models import Products


class ProductsSitemap(Sitemap):
    def items(self):
        return  Products.objects.all()



