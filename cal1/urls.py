from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('binary.html/',views.binary,name="binary"),
    path('binary.html/bi',views.bi,name="bi"),
    path('decimal.html/',views.decimal,name="decimal"),
    path('decimal.html/dl',views.dl,name="dl"),
    path('MaSD.html/',views.masd,name="masd"),
    path('MaSD.html/cal',views.cal,name="cal"),
    path('agecal.html/',views.agecal,name="agecal"),
    path('agecal.html/age',views.age,name="age"),
   path('calbmi.html/',views.calbmi,name="calbmi"),
   path('calbmi.html/bmi',views.bmi,name="bmi"),
   path('logcal.html/',views.logcal,name="logcal"),
   path('logcal.html/log',views.log,name="log")

]