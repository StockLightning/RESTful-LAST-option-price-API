# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^getlastprice', views.getlastprice),
]
