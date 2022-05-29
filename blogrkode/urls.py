from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('Programing/<tipe>',views.home_Programing,name='home_Programing'),
    path('Project/<tipe>',views.home_Project,name='home_Project'),
    path('Programing/<tipe>/<slug>',views.detail_Programing,name='detail_Programing'),
    path('Project/<tipe>/<slug>',views.detail_Project,name='detail_Project'),
    # path('register/' , views.register_view , name="register_view"),
    # path('verify/<token>/' , views.verify , name="verify"),
]
