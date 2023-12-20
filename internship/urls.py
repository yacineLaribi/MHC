from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.internships,name='browse'),
    path('new/',views.new,name="new"),
]
