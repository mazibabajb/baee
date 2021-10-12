"""ecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path,include
from django.urls.conf import re_path
from Djangoecormeceapp import views
from Djangoecormeceapp import AdminView
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from Djangoecormeceapp.sitemaps import ProductsSitemap
from blog.sitemaps import PostSitemap
from books.sitemaps import BookSitemap

sitemaps={
    'Products':ProductsSitemap,
    'PostSitemap':PostSitemap,
    'Books': BookSitemap,
    
    }


urlpatterns = [
    path('main_admin/', admin.site.urls),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('',include("Djangoecormeceapp.front_end_urls")),
    path('admin_dashboard/',include("Djangoecormeceapp.adminurls")),
    path('merchant_dashboard/',include("Djangoecormeceapp.merchant_urls")),
    path('affilliate_dashboard/',include("Djangoecormeceapp.affilliate_urls")),
    path('blog/',include("blog.urls")),
    path('books/',include("books.urls")),
    path('cart/',include("cart.urls",namespace="cart")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    
    
]
