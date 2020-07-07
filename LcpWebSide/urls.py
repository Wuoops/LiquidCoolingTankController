from django.contrib import admin
from django.urls import path
from homePage.views import homepage,homePage
from django.conf.urls import url
from sensorFront.views import sensor
from setup.views import setup
from server.views import *
from tank.views import cdu,getLevel
from sensorFront.views import *



urlpatterns = [
    url(r'^$',homepage),
    path('admin/', admin.site.urls),
    url(r'^homepage/',homepage),
    url(r'^homePage/',homePage),
    url(r'^sensor/',sensor),
    url(r'^setup/',setup),
    url(r'^server/',server),
    url(r'^cdu/',cdu),
    url(r'^getSensorData/',getSensorData),
    url(r'^getBmcData/',getBmcData),
    url(r'^getcpuData/',getcpuData),
    url(r'^serverNode/',serverNode),
    url(r'^getLevel/',getLevel),
]
