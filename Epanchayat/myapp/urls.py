from django.contrib import admin
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name='index'),
    path("about/",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    #path("loginstaff/",views.loginstaff,name='loginstaff'),
    path("logoutstaff",views.logoutstaff,name='logoutstaff'),
    path("stafflogout",views.staff_logout,name='stafflogout'),
    path("feedback",views.feedback,name='feedback'),
    path("aboutus",views.aboutus,name='aboutus'),
    path("complaints",views.complaints,name='complaints'),
    path("logins",views.logins,name='logins'),
    path("password_reset/",auth_views.PasswordResetView.as_view(),name="password_reset"),
    path("password_reset/done/",auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path("addandshow",views.add_show,name='addandshow'),
    path('delete/<int:service_id>/',views.delete_service,name='deleteservice'),
    path('<int:service_id>/',views.update_service,name='updateservice'),
    path('applyservice/<int:service_id>/',views.apply_service,name='applyservice'),
    path("bbb",views.bbb,name='bbb'),
    #path('',views.service_A,name='service_A')
    #path('job',views.job.as_view(),name='job'),
     path("showappl",views.showappl,name='showappl'),
]

#1.submit email form                        //passwordResetView.as_view()
#2-Email sent success message               //passwordResetDoneView.as_view()
#3.link to password reset form in email     //passwordResetConfirmView.as_view()
#4-password successfuly changed message     //PaswordResetCompleteView.as_view()