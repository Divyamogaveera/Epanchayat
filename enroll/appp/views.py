from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from datetime import  datetime
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import logout 
from .forms import SignUpForm
from django.views.decorators.cache import never_cache
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

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
       # contact=Contact(name=name,email=email,phone=phone,GramPanchayat=GramPanchayat,info=info,adinfo=adinfo,date=datetime.today())
        contact.save()
        messages.success(request, 'Information has been sent...')



    return render(request,'contact.html')
    #return HttpResponse('contact')


def logins(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
         #CHECK USERS CREDENTIALS
        User = authenticate(username=username,password=password)
        if User is not None:
            auth_login(request,User)
            return render(request,'logins.html')
        else:
            return render(request,'loginstaff.html')

    return render(request,'loginstaff.html')

def logoutstaff(request):
    logout(request)
    return redirect("/logins")
   # return HttpResponse('services')

def loginstaff(request):
    if request.user.is_anonymous:
        return redirect("/logins")
    return render(request,'logins.html')
    #@never_cache 
   # def loginstaff(request):
     #if User.is_authenticated:
      #   return HttpResponseRedirect(reversed('logins.html'))
#registration for panchayat users and then login joiningbthe users group
def sign_up(request):
 if request.method == "POST":
     fm= SignUpForm(request.POST)
     if fm.is_valid():
         messages.success(request,'account created')
         fm.save()
 else:
     fm = SignUpForm()
 return render(request,'signup.html',{'form':fm})
