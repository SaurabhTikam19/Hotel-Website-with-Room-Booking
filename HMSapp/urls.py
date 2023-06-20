from django.contrib import admin
from django.urls import path, include
from HMSapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('coupleroom',views.couple, name='couple'),
    path('familyroom',views.family, name='family'),
    path('villa',views.villa, name='villa'),
    path('login',views.login, name='login'),
]