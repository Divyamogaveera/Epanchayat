from django.contrib import messages
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect,HttpResponseRedirect
from datetime import  datetime
from django.views.generic import TemplateView
from django.utils.translation import templatize
from .models import Contact, Feedback,Complaints
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login as auth_login,login
from django.contrib.auth import logout , update_session_auth_hash
from django.contrib.auth import logout as stafflogout
from .forms import  SignUpForm, EditUserDetailsForm , EditAdminDetailsForm,ServiceRegistration,ServicebForm
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.conf import settings
#from django.views import View
from .models import User,service,service_A,Service_B
from myapp.managers import CustomUserManager
#from myapp.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL
#Use get_user_model() method instead (you can import it from django.contrib.auth import get_user_model).
#  settings.AUTH_USER_MODEL is just a string, which can be used when you define a model,
#  (e.g. ForeignKey accepts a string) but not when you need the actual class
from django.contrib.auth import get_user_model
User = get_user_model()




# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
   # return HttpResponse('about')

def bbb(request):
    return render(request,'bbb.html')

def aboutus(request):
    return render(request,'about.html')

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        grampanchayat=request.POST.get('grampanchayat')
        info=request.POST.get('info')
        adinfo=request.POST.get('adinfo')
        contact=Contact(name=name,email=email,phone=phone,gender=gender,grampanchayat=grampanchayat,info=info,adinfo=adinfo,date=datetime.today())
        contact.user=request.user
        contact.save()
        messages.success(request, 'Information has been sent...')
    return render(request,'contact.html')
    #return HttpResponse('contact')

#ratings
def feedback(request):
        if request.method =="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            grampanchayat=request.POST.get('grampanchayat')
            rate=request.POST.get('rate')
            adinfo=request.POST.get('adinfo')
            feedback=Feedback(name=name,email=email,phone=phone,grampanchayat=grampanchayat,rate=rate,adinfo=adinfo,date=datetime.today())
            feedback.user=request.user
            feedback.save()
            messages.success(request, 'Information has been sent...')
        
        return render(request,'feedback.html')

#ratings
def complaints(request):
        if request.method =="POST":
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            complaint=request.POST.get('complaint')
            complaints=Complaints(firstname=firstname,lastname=lastname,email=email,gender=gender,complaint=complaint,date=datetime.today())
            complaints.user=request.user
            complaints.save()
            #{'alert_flag':True}
            messages.success(request, 'Information has been sent...')
            
        
        return render(request,'comp.html')
        


def logoutstaff(request):
        logout(request)
        messages.info(request,'You have been loged out.')
        return redirect("/loginstaff")

   # return HttpResponse('services')

#def loginstaff(request):
  #if not request.user.is_authenticated:
    # get all the users of the group writer
    #users_in_group = Group.objects.get(name="writer").user_set.all()
    # only if that user is a part the group
    #if request.method == "POST" and request.user in users_in_group :
    #... #the rest of your function here  

def loginstaff(request):
    if not request.user.is_authenticated:
        users_in_group = Group.objects.get(name="STAFF").user_set.all()
        if request.method == "POST" :
            fm= AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname= fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                User = authenticate(username=uname,password=upass)
                if User is not None:
                    #I put this line here :
                    if  User in users_in_group :
                        login(request,User)
                        messages.success(request,'Logged in Successfully..!')
                        return HttpResponseRedirect('/staffprofile/')
                    else:
                        messages.info(request,'You are not allowed to login')

        else:
            fm=AuthenticationForm()
            return render(request,'loginstaff.html',{'form':fm})
    else:
        logout(request)
        return redirect("loginstaff/")
        
        #return HttpResponseRedirect('/staffprofile/')
    #@never_cache 
   # def loginstaff(request):
     #if User.is_authenticated:
      #   return HttpResponseRedirect(reversed('logins.html'))
#registration for panchayat users and then login joiningbthe users group
def sign_up(request):
    if request.method == "POST":
        fm= SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully..:)')
            fm.save()
            user = fm.save()
            group = Group.objects.get(name='USERS')
            user.groups.add(group)
    else:
        fm = SignUpForm()
    return render(request,'signup.html',{'form':fm})

#login view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm= AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname= fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                User = authenticate(username=uname,password=upass)
                if User is not None:
                    auth_login(request,User)
                    messages.success(request,'Logged in Successfully..!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm=AuthenticationForm()
        return render(request,'userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

#profile
def user_profile(request):
    if request.user.is_authenticated:
        stud= service.objects.all()
        return render(request,'profile.html',{'stu':stud,'name':request.user})
    else:
        return HttpResponseRedirect('/userlogin/')

def showappl(request):
        studd= service_A.objects.all()
        return render(request,'showappl.html',{'stuu':studd,'name':request.user})
    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/userlogin/')


    #login view
#def staff_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm= AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname= fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                User = authenticate(username=uname,password=upass)
                if User is not None:
                    login(request,User)
                    messages.success(request,'Logged in Successfully..!')
                    return HttpResponseRedirect('/staffprofile/')
        else:
            fm=AuthenticationForm()
        return render(request,'stafflogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/staffprofile/')

#profile
def staff_profile(request):
    if request.user.is_authenticated:
        return render(request,'staffprofile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/loginstaff')

def staff_logout(request):
    stafflogout(request)
    return HttpResponseRedirect('/logins')

#user password chenge using old password
def user_change_pass(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully..')
                return HttpResponseRedirect('/changepass/')
            #else:
                #messages.info(request,'please enter proper details..') 
                #fm=PasswordChangeForm(user=request.user)
                #return render(request,'changepass.html',{'form':fm})       
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'changepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userlogin/')

def user_change_pass2(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully..')
                return HttpResponseRedirect('/changepass2/')
            #else:
                #messages.info(request,'please enter proper details..') 
                #fm=PasswordChangeForm(user=request.user)
                #return render(request,'changepass.html',{'form':fm})       
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'changepass2.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userlogin/')

def staff_change_pass(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully..')
                return HttpResponseRedirect('/staffchangepass2/')
            #else:
                #messages.info(request,'please enter proper details..') 
                #fm=PasswordChangeForm(user=request.user)
                #return render(request,'staffchangepass.html',{'form':fm})       
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'staffchangepass.html',{'form':fm})
    else:
        return HttpResponseRedirect('/loginstaff')

def staff_change_pass2(request):
    if  request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password changed successfully..')
                return HttpResponseRedirect('/staffchangepass/')
            #else:
                #messages.info(request,'please enter proper details..') 
                #fm=PasswordChangeForm(user=request.user)
                #return render(request,'staffchangepass.html',{'form':fm})       
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'staffchangepass2.html',{'form':fm})
    else:
        return HttpResponseRedirect('/loginstaff')

#userdetails
def user_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminDetailsForm(request.POST,instance=request.user)
                #users= admin
                users= User.objects.all()
                #users= None
            else:
                fm=EditUserDetailsForm(request.POST,instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request,'changes has been applied,now you can edit more')
                fm.save()
        else: 
            if request.user.is_superuser == True:
                fm = EditAdminDetailsForm(instance=request.user)
                users= User.objects.all()
                #users=None
            else:
                 fm = EditUserDetailsForm(instance=request.user)
                 users=None
        return render(request,'userdetails.html', {'name':request.user, 'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/userlogin/')

def staff_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = EditAdminDetailsForm(request.POST,instance=request.user)
                users= User.objects.all()
                #users=None
            else:
                fm=EditUserDetailsForm(request.POST,instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request,'changes has been applied, now you can edit more')
                fm.save()
        else: 
            if request.user.is_superuser == True:
                fm = EditAdminDetailsForm(instance=request.user)
                users= User.objects.all()
                #users=None
            else:
                 fm = EditUserDetailsForm(instance=request.user)
                 users=None
        return render(request,'staffdetails.html', {'name':request.user, 'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/loginstaff')

def pusers(request,user_id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=user_id)
        fm = EditAdminDetailsForm(instance=pi)
        return render(request, 'pusers.html',{'form':fm})
    else:
        return HttpResponseRedirect('/userlogin/')

def susers(request,user_id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=user_id)
        fm = EditAdminDetailsForm(instance=pi)
        return render(request, 'susers.html',{'form':fm})
    else:
        return HttpResponseRedirect('/loginstaff')


def logins(request):
    if not request.user.is_authenticated:
        users_in_group = Group.objects.get(name="STAFF").user_set.all()
        if request.method == "POST" :
            fm= AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname= fm.cleaned_data['username']
                upass= fm.cleaned_data['password']
                User = authenticate(username=uname,password=upass)
                if User is not None:
                    #I put this line here :
                    if  User in users_in_group :
                        login(request,User)
                        messages.success(request,'Logged in Successfully..!')
                        #return HttpResponseRedirect('/staffprofile/')
                        return HttpResponseRedirect('/addandshow')
                    else:
                        messages.info(request,'You are not allowed to login')

        else:
            fm=AuthenticationForm()
        return render(request,'loginstaff.html',{'form':fm})
    else:
        logout(request)
        return HttpResponseRedirect('/logins')
        #return redirect("/logins/")


class ModelView(TemplateView):
    template_name = "userdetails.html"
    
    def get_context_data(self, **kwargs):
        context = super(ModelView.self).get_context_data(**kwargs)
        context["object_list"] = User.objects.all()
        return context


# this function will add and show services
#fm=ServiceRegistration(request.POST)
        #if fm.is_valid():
            #fm.save()

def add_show(request):
    if request.method=='POST':
        fm=ServiceRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['service_name']
            dec=fm.cleaned_data['description']
            rec=fm.cleaned_data['requirements']
            reg=service(service_name=nm,description=dec,requirements=rec)
            reg.user=request.user
            reg.save()
            fm=ServiceRegistration()
    else:
        fm=ServiceRegistration()
    fm=ServiceRegistration()
    stud= service.objects.all()
    return render(request,'svs/addandshow.html',{'form':fm,
    'stu':stud})

#deleting services
def delete_service(request,service_id):
    if request.method=='POST':
        pi=service.objects.get(pk=service_id)
        pi.delete()
        return HttpResponseRedirect('/addandshow')

#edit/updating services
def update_service(request,service_id):
    if request.method=='POST':
        pi=service.objects.get(pk=service_id)
        fm=ServiceRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=service.objects.get(pk=service_id)
        fm=ServiceRegistration(instance=pi)
    return render(request,'svs/updateservice.html',{'form':fm})

#application
def apply_service(request,service_id):
    #service_id=get_object_or_404(service,pk=service_id)
    if service_id==1:
        if request.method=="POST":
            service_name=request.POST.get('service_name')
            user_name=request.POST.get('user_name')
            #if len(request.FILES)!=0:
            user_image=request.FILES['user_image']
            #user_image.save()
            #messages.success(request,'success')
            #user_image=request.POST.get('user_image')
            firstname=request.POST.get('firstname')
            lastname=request.POST.get('lastname')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            wardno=request.POST.get('wardno')
            grampanchayat=request.POST.get('grampanchayat')
            phone=request.POST.get('phone')
            village=request.POST.get('village')
            city=request.POST.get('city')
            state=request.POST.get('state')
            pin_code=request.POST.get('pin_code')
            adhar_no=request.POST.get('adhar_no')
            adhar_img=request.FILES['adhar_img']
            #incom_proof=request.FILES.getlist("incom_proof")
            incom_proof=request.FILES['incom_proof']
            #for f in incom_proof:
                #service_A(incom_proof=f).save()
            vote=request.FILES.getlist("vote")
            #apply_date=request.POST.get('apply_date')
            for vote in vote:
                seervice_A=service_A(service_name=service_name,user_name=user_name,user_image=user_image,firstname=firstname,lastname=lastname,email=email,gender=gender,wardno=wardno,grampanchayat=grampanchayat,phone=phone,village=village,city=city,state=state,pin_code=pin_code,adhar_no=adhar_no,adhar_img=adhar_img, incom_proof= incom_proof,vote=vote,apply_date=datetime.today())
                seervice_A.user=request.user
                #seervice_A.service_id=request.service_id
                seervice_A.save()
                messages.success(request, 'Information has been sent...')
        studd= service_A.objects.all()
        return render(request,'svs/servicea.html',{'service_id':service_id,'stuu':studd})
    elif service_id==2:
        form=ServicebForm()
        if request.method=="GET":
            form=ServicebForm()
            return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
        if request.method=="POST":
            form=ServicebForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                #form=ServicebForm()
                return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
            else:
                return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
        return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
    elif service_id==3:
        return render(request,'svs/servicec.html',{'service_id':service_id})
    elif service_id==4:
        return render(request,'svs/serviced.html',{'service_id':service_id})
    else:
        return render(request,'svs/servicez.html',{'service_id':service_id})

#def service_A(request):
    #if request.method=="POST":
        #fm=ApplyForServiceA(request.POST)
        if fm.is_valid():
            messages.success(request,'APPLIED SUCCESSFULLY')
            fm.save()
    #else:
        fm=ApplyForServiceA()
    #return render(request,'servicea.html',{'form':fm})

#class job(View):
    def get(self,request):
        form=ServicebForm()
        return render(request,'serviceb.html',{'form':form})





    







   