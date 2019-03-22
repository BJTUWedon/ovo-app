"""OvO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
# from django.contrib import admin
from django.conf.urls import *
import settings


#urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
# ]
urlpatterns = patterns('',
    url(r'^$', 'OvO.views.home'),
    url(r'^admin/', include('Admin.urls')),
    url(r'^face_analysis/', include('Face_Analysis.urls')),
    url(r'^decision_tree/', include('Decision_Tree.urls')),
    # url(r'^wear_glass/', include('Wear_Glass.urls')),
    url(r'^contact/', include('Contact.urls')),
    url(r'^Getphotos/', 'OvO.views.Getphotos'),
    # url(r'^Analysis/', 'Face_Analysis.face_token.face_token'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
    url(r'^base64/', 'Face_Analysis.face_token.face_token'),
    url(r'^wear/', 'Wear_Glass.wear.wearglass'),
    url(r'^Wear_Glass/','OvO.views.Wear_Glass'),
    # url(r'^base64/', 'Face_Analysis.base64.add_face_data')
)