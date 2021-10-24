from django.contrib import messages
from django.contrib.messages.api import error
from django.http import request
from django.core.exceptions import ValidationError
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import  render,redirect,HttpResponseRedirect
from datetime import  datetime
from django.db import IntegrityError
from django.views.generic import TemplateView
from django.utils.translation import templatize
from .models import Contact, Feedback,Complaints, service_C, service_Z
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate,login as auth_login,login
from django.contrib.auth import logout , update_session_auth_hash
from django.contrib.auth import logout as stafflogout
from .forms import  SignUpForm, EditUserDetailsForm , EditAdminDetailsForm,ServiceRegistration,ServicebForm,ServicecForm,ServicezForm,ServiceaForm
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.conf import settings
#from django.views import View
from .models import User,service,service_A,Service_B,approve1,approve2,approve3,approve4
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

def big(request):
    studd= service_A.objects.all()
    studdd=Service_B.objects.all()
    return render(request,'big.html',{'stuu':studd,'name':request.user,'stuuu':studdd,'name':request.user})

def big2(request):
    studdd=Service_B.objects.all()
    return render(request,'big2.html',{'name':request.user,'stuuu':studdd,})

def big3(request):
    studdd=service_C.objects.all()
    return render(request,'big3.html',{'name':request.user,'stuuu':studdd,})

def sz(request):
    studd=service_Z.objects.all()
    return render(request,'sz.html',{'name':request.user,'stuu':studd,})


def servicestatus(request):
    return render(request,'servicestatus.html')

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

def showapprove1(request):
    apr=approve1.objects.all()
    return render(request,'showapprove1.html',{'apr':apr})

def showapprove2(request):
    aprr=approve2.objects.all()
    return render(request,'showapprove2.html',{'aprr':aprr})

def showapprove3(request):
    aprrr=approve3.objects.all()
    return render(request,'showapprove3.html',{'aprrr':aprrr})

def showapprove4(request):
    aprrrr=approve4.objects.all()
    return render(request,'showapprove4.html',{'aprrrr':aprrrr})

def showappl(request):
        studd= service_A.objects.all()
        studdd=Service_B.objects.all()
        studddd=service_C.objects.all()
        studdddd=service_Z.objects.all()
        return render(request,'showappl.html',{'stuu':studd,'stuuu':studdd,'stuuuu':studddd,'stuuuuu':studdddd})

def showappr1(request):
        studd= service_A.objects.all()
        return render(request,'approve1.html',{'stuu':studd})
        

def showappl2(request):
        studd= service_A.objects.all()
        studdd=Service_B.objects.all()
        studddd=service_C.objects.all()
        studdddd=service_Z.objects.all()
        return render(request,'showappl2.html',{'stuu':studd,'stuuu':studdd,'stuuuu':studddd,'stuuuuu':studdddd})
        

def showappl3(request):
        studd= service_A.objects.all()
        studdd=Service_B.objects.all()
        studddd=service_C.objects.all()
        studdddd=service_Z.objects.all()
        return render(request,'showappl3.html',{'stuu':studd,'stuuu':studdd,'stuuuu':studddd,'stuuuuu':studdddd})
        
def showappl4(request):
        studd= service_A.objects.all()
        studdd=Service_B.objects.all()
        studddd=service_C.objects.all()
        studdddd=service_Z.objects.all()
        return render(request,'showappl4.html',{'stuu':studd,'stuuu':studdd,'stuuuu':studddd,'stuuuuu':studdddd})
        

    

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
            messages.success(request, 'Information has been sent...')
            fm=ServiceRegistration()
        else:
            messages.success(request, 'service name is already exist')
            fm=ServiceRegistration()
    else:
        fm=ServiceRegistration()
    fm=ServiceRegistration()
    stud= service.objects.all()
    return render(request,'svs/addandshow.html',{'form':fm,
    'stu':stud})

def shows(request):
        stud= service.objects.all()
        return render(request,'svs/shows.html',{'stu':stud,})

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
            messages.success(request, 'Information has been sent...')
    else:
        pi=service.objects.get(pk=service_id)
        fm=ServiceRegistration(instance=pi)
    return render(request,'svs/updateservice.html',{'form':fm})

#def update_service2(request,job_id):
    if request.method=="GET":
                form=ApproveForm()
                return render(request,'svs/updateservice2.html',{'job_id':job_id,'form':form})
    if request.method=="POST":
                form=ApproveForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Information has been sent...')
                    #form=ServicebForm()
                    return render(request,'svs/updateservice2.html',{'job_id':job_id,'form':form})
                else:
                    return render(request,'svs/updateservice2.html',{'job_id':job_id,'form':form})
    form=ApproveForm()
    return render(request,'svs/updateservice2.html',{'job_id':job_id,'form':form})
        #if request.method=='':
        #pi=Service_B.objects.get(pk=job_id)
        #fm=ApproveForm(request.POST,instance=pi)
        #if fm.is_valid():
            #fm.save()
            #messages.success(request, 'Information has been sent...')
    #else:
        #pi=Service_B.objects.get(pk=job_id)
        #fm=ApproveForm(instance=pi)
    #return render(request,'svs/updateservice2.html',{'form':fm})

#application
def apply_service(request,service_id):
    #service_id=get_object_or_404(service,pk=service_id)
    if service_id==1:
        if request.method=="GET":
            form=ServiceaForm()
            return render(request,'svs/servicea.html',{'service_id':service_id,'form':form})
        if request.method=="POST":
            form=ServiceaForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Information has been sent...')
                #form=ServicebForm()
                return render(request,'svs/servicea.html',{'service_id':service_id,'form':form})
            else:
                return render(request,'svs/servicea.html',{'service_id':service_id,'form':form})
        form=ServiceaForm()
        return render(request,'svs/servicea.html',{'service_id':service_id,'form':form})
    elif service_id==2:
        #form=ServicebForm()
        if request.method=="GET":
            form=ServicebForm()
            return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
        if request.method=="POST":
            form=ServicebForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Information has been sent...')
                #form=ServicebForm()
                return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
            else:
                return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
        form=ServicebForm()
        return render(request,'svs/serviceb.html',{'service_id':service_id,'form':form})
    elif service_id==3:
       if request.method=="GET":
            formc=ServicecForm()
            return render(request,'svs/servicec.html',{'service_id':service_id,'formc':formc})
       if request.method=="POST":
            formc=ServicecForm(request.POST,request.FILES)
            if formc.is_valid():
                formc.save()
                messages.success(request, 'Information has been sent...')
                #form=ServicebForm()
                return render(request,'svs/servicec.html',{'service_id':service_id,'formc':formc})
            else:
                return render(request,'svs/servicec.html',{'service_id':service_id,'formc':formc})
       formc=ServicecForm()
       return render(request,'svs/servicec.html',{'service_id':service_id,'formc':formc})
    elif service_id==4:
        if request.method=="POST":
            formz=ServicezForm(request.POST,request.FILES)
            if formz.is_valid():
                formz.save()
                messages.success(request, 'Information has been sent...')
                #form=ServicebForm()
                return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})
            else:
                return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})
        elif request.method=="GET":
            formz=ServicezForm()
            return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})
        formz=ServicezForm()
        return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})
    else:
        if request.method=="POST":
            formz=ServicezForm(request.POST,request.FILES)
            if formz.is_valid():
                formz.save()
                messages.success(request, 'Information has been sent...')
                #form=ServicebForm()
                return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})
            else:
                return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})
        elif request.method=="GET":
            formz=ServicezForm()
            return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})
        formz=ServicezForm()
        return render(request,'svs/servicez.html',{'service_id':service_id,'formz':formz})

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


def approve_service1(request,income_id,):
        if request.method=="POST":
                try:
                    income_no=request.POST.get('income_no')
                    name=request.POST.get('name')
                    houseno=request.POST.get('houseno')
                    decision=request.POST.get('decision')
                    approvee=approve1(income_no=income_no,name=name,houseno=houseno,decision=decision)
                    #approve.user=request.user
                    approvee.save()
                    messages.success(request, 'Information has been sent...')
                except IntegrityError:
                    messages.success(request, 'You have already made decision for this applicant')
        studd=service_A.objects.all()
        return render(request,'approve1.html',{'income_id':income_id,'stuu':studd})
    #return HttpResponse('contact')

def approve_service2(request,job_id,):
        if request.method=="POST":
                try:
                    job_no=request.POST.get('job_no')
                    name=request.POST.get('name')
                    email=request.POST.get('email')
                    decision=request.POST.get('decision')
                    approvee=approve2(job_no=job_no,name=name,email=email,decision=decision,)
                    #approve.user=request.user
                    approvee.save()
                    messages.success(request, 'Information has been sent...')
                except IntegrityError:
                    messages.success(request, 'You have already made decision for this candidate')
        studdd=Service_B.objects.all()
        return render(request,'approve2.html',{'job_id':job_id,'stuuu':studdd})

def approve_service3(request,gas_id,):
        if request.method=="POST":
                try:
                    gas_no=request.POST.get('gas_no')
                    name=request.POST.get('name')
                    ration_no=request.POST.get('ration_no')
                    decision=request.POST.get('decision')
                    approvee=approve3(gas_no=gas_no,name=name,ration_no=ration_no,decision=decision)
                    #approve.user=request.user
                    approvee.save()
                    messages.success(request, 'Information has been sent...')
                except IntegrityError:
                    messages.success(request, 'You have already made decision for this ration no')
        studdd=service_C.objects.all()
        return render(request,'approve3.html',{'gas_id':gas_id,'stuuuu':studdd})

def approve_service4(request,curr_id,):
        if request.method=="POST":
                try:
                    curr_no=request.POST.get('curr_no')
                    service_name=request.POST.get('service_name')
                    keyno=request.POST.get('keyno')
                    decision=request.POST.get('decision')
                    approvee=approve4(curr_no=curr_no,service_name=service_name,keyno=keyno,decision=decision,)
                    #approve.user=request.user
                    approvee.save()
                    messages.success(request, 'Information has been sent...')
                except IntegrityError:
                    messages.success(request, 'You have already made decision for this keyno')
                    
                
        studdd=service_Z.objects.all()
        return render(request,'approve4.html',{'curr_id':curr_id,'stuuuuu':studdd})







    







   