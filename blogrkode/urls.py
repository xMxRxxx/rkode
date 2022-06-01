from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from blogrkode.sitemaps import blogSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'blog' : blogSitemap
}
urlpatterns = [
    path('',views.home,name='home'),
    path('Programing/<tipe>',views.home_Programing,name='home_Programing'),
    path('Project/<tipe>',views.home_Project,name='home_Project'),
    path('Programing/<tipe>/<slug>',views.detail_Programing,name='detail_Programing'),
    path('Project/<tipe>/<slug>',views.detail_Project,name='detail_Project'),
    # path('<id>',views.detail,name='detail'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    # path('register/' , views.register_view , name="register_view"),
    # path('verify/<token>/' , views.verify , name="verify"),
]
