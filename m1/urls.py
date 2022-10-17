
from django.views import View
from . import views
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Welcome to FindyourDoctor+ Pannel"


urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="aboutus"),
    path('contactus', views.contactus, name="contact"),
    path('search', views.search, name="search"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)