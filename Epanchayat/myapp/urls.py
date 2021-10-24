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
    path("shows",views.shows,name='shows'),
    path('delete/<int:service_id>/',views.delete_service,name='deleteservice'),
    path('<int:service_id>/',views.update_service,name='updateservice'),
    path('applyservice/<int:service_id>/',views.apply_service,name='applyservice'),
    path("bbb",views.bbb,name='bbb'),
    #path('',views.service_A,name='service_A')
    #path('job',views.job.as_view(),name='job'),
    path("showappl",views.showappl,name='showappl'),
    path("showappl2",views.showappl2,name='showappl2'),
    path("showappl3",views.showappl3,name='showappl3'),
    path("showappl4",views.showappl4,name='showappl4'),
    #path('showappl/<int:job_id>/',views.update_service2,name='updateservice2'),
    path('showappl/<int:income_id>/',views.approve_service1,name='approve_service1'),
    path('showappl2/<int:job_id>/',views.approve_service2,name='approve_service2'),
    path('showappl3/<int:gas_id>/',views.approve_service3,name='approve_service3'),
    path('showappl4/<int:curr_id>/',views.approve_service4,name='approve_service4'),
    path('big',views.big,name='big'),
    path('sz',views.sz,name='sz'),
    path("big2",views.big2,name='big2'),
    path("big3",views.big3,name='big3'),
    path("showapprove1",views.showapprove1,name='showapprove1'),
    path("showapprove2",views.showapprove2,name='showapprove2'),
    path("showapprove3",views.showapprove3,name='showapprove3'),
    path("showapprove4",views.showapprove4,name='showapprove4'),
    path("servicestatus",views.servicestatus,name='servicestatus'),
    
]

#1.submit email form                        //passwordResetView.as_view()
#2-Email sent success message               //passwordResetDoneView.as_view()
#3.link to password reset form in email     //passwordResetConfirmView.as_view()
#4-password successfuly changed message     //PaswordResetCompleteView.as_view()