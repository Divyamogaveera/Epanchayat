from django.contrib import messages
from django.shortcuts import render,redirect
from datetime import  datetime
from .models import Contact
from django.contrib import messages




# Create your views here.
def index(request):
    context={
    'variable1':"this is divya",
    'variable2':"this is depression"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
   # return HttpResponse('about')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        GramPanchayat=request.POST.get('GramPanchayat')
        info=request.POST.get('info')
        adinfo=request.POST.get('adinfo')
        contact=Contact(name=name,email=email,phone=phone,GramPanchayat=GramPanchayat,info=info,adinfo=adinfo,date=datetime.today())
        contact.save()
        messages.success(request, 'Information has been sent...')



    return render(request,'contact.html')
    #return HttpResponse('contact')

def services(request):
    return render(request,'logout.html')
   # return HttpResponse('services')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'index.html')
   # return HttpResponse('services')