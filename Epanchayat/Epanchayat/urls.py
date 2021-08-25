"""Epanchayat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp import views
import myapp

admin.site.site_header = "Panchayat services Admin"
admin.site.site_title = "panchayat services Admin Portal"
admin.site.index_title = "panchayat services Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("",views.home,name='index'),
    path('',include('myapp.urls')),
    path('signup/',views.sign_up,name='signup'),
    path('userlogin/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    #path("loginstaff/",views.loginstaff,name='loginstaff'),
    #path('loginstaff/',views.loginstaff,name='loginstaff'),
    #path('logins/',views.logins,name='logins'),
    #path('stafflogin/',views.staff_login,name='stafflogin'),
    path('stafflogout/',views.staff_logout,name='stafflogout'),
    path('staffprofile/',views.staff_profile,name='staffprofile'),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('staffchangepass/',views.staff_change_pass,name='staffchangepass'), 
    path('userdetails/',views.user_details,name='userdetails'),
    path('pusers/<int:id>',views.pusers,name='pusers'),
    path('staffdetails/',views.staff_details,name='staffdetails'),
    path('susers/<int:id>',views.susers,name='susers'),
    path('staffchangepass2/',views.staff_change_pass2,name='staffchangepass2'), 
    path('changepass2/',views.user_change_pass2,name='changepass2'),

    
]
