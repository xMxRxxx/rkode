"""rkode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from blogrkode.sitemaps import blogSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'blog' : blogSitemap
}

urlpatterns = [
    
    path('', include('blogrkode.urls')),
    path('Programing/<tipe>',include('blogrkode.urls')),
    path('Project/<tipe>',include('blogrkode.urls')),
    path('robots.txt', include('robots.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    # path("register/", include('blogrkode.urls')),
    # path('verify/<token>/' ,include('blogrkode.urls')),
    path('momonga-page/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
