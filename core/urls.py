from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    
]
