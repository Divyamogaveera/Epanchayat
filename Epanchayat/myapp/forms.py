
from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from django.forms import widgets
from django.http import request
from .models import GENDER_CHOICE, JOB_PANCHAYAT, User, service_A, service_C
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User,service,Contact,Service_B,service_C,service_Z
from myapp.models import User
from django.core import validators
#from django.conf import settings
#User = settings.AUTH_USER_MODEL
#class MyModelForm(forms.ModelForm):
    #class Meta:
       # models=User
        #widgets={
            #'Birth_date':forms.TextInput(attrs={'placeholder':'name'}),
        #}


class SignUpForm(UserCreationForm):
    #def __init__(self, *args, **kwargs):
       # super().__init__(*args, **kwargs)
       # self.fields['wardno'].required=True
    
    #phone=forms.CharField()
    #wardno=forms.CharField()
    #Birth_date=forms.DateField()
    #grampanchayat=forms.CharField()
    password1= forms.CharField(label='Enter Password',
    widget=forms.PasswordInput) 
    password2= forms.CharField(label='ReenterPassword',
    widget=forms.PasswordInput)    
    class Meta:
        model=User
        widgets={
            'Birth_date':forms.TextInput(attrs={'placeholder':'DD/MM/YY'}),
            'email':forms.TextInput(attrs={'placeholder':'youremail12@gmail.com'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
        }
        fields = ['username','first_name','last_name','email','gender','Birth_date','phone','wardno','grampanchayat',]
        labels={'username':'User Name'}
        labels={'first_name':'FirstName'}
        labels={'last_name':'LastName'}
        labels={'email':'E-mail :'}
        labels={'wardno':'Ward-No:'}
        
        

        #def __init__(self, *args, **kwargs):
           # super(SignUpForm, self).__init__(*args, **kwargs)
           # self.fields['email'].required=True
        
            
#userdetails
class EditUserDetailsForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','gender','Birth_date','date_joined','last_login','phone','wardno','grampanchayat']
        labels = {'email':'Email'}

#admin details
class EditAdminDetailsForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','gender','Birth_date','wardno','date_joined','last_login','phone','is_superuser','is_staff','is_active','date_joined']
        #fields='__all__'
        labels = {'email':'Email'}

class ServiceRegistration(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ServiceRegistration,self).__init__(*args,**kwargs)
        #self.fields['service_name'].required=True
        self.fields['description'].required=True
        self.fields['requirements'].required=True
    class Meta:
        model = service
        fields=['service_id','service_name','description','requirements']
        widgets={
            'service_name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.TextInput(attrs={'class':'form-control'}),
            'requirements':forms.Textarea(attrs={'class':'form-control','rows':4}),
        }

#class ContactForm(forms.ModelForm):
    #class Meta:
        #model = Contact
        #fields=['contact_id','user','name','email','gender','phone','grampanchayat','wardno','info','adinfo',]

#Service_A form for Ration card
#class ApplyForServiceA(forms.ModelForm):
    #class Meta:
        #model=service_A
        #fields=['service_name','user_name','user_image','firstname','lastname','email','gender','wardno','grampanchayat',
        #'village','city','state','pin_code','adhar_no','adhar_img','incom_proof','vote','apply_date']
GENDER_CHOICE=[
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHERS','OTHERS')
    ]
JOB_PANCHAYAT=(
    ('Aloor','Aloor'),
    ('Kota','Kota'),
    ('Kundapur','Kundapur')
)
PANCHAYAT=(
    ('aloor','aloor'),
    ('kota','kota'),
    ('kumdapur','kundapur')
)
DECISION_CHOICE=(
    ('APPROVE','APPROVE'),
    ('DECLINE','DECLINE'),
)
class ServicebForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ServicebForm,self).__init__(*args,**kwargs)
        self.fields['email'].required=True
        self.fields['document'].required=True
        self.fields['panchayat'].required=True
        self.fields['job_panchayat'].required=True
        self.fields['mobile'].required=True
        self.fields['village'].required=True
        self.fields['hscssc'].required=True
        self.fields['profile_img'].required=True
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    #panchayat=forms.ChoiceField(choices=PANCHAYAT,widget=forms.Select(attrs={'class':'form-control'}))
    #job_panchayat=forms.Mult
    # ipleChoiceField(label='prefered job location',choices=JOB_PANCHAYAT,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Service_B
        fields=['job_id','name','dob','gender','village','city','pin','state','mobile','email','panchayat','job_panchayat','profile_img','hscssc','document']
        labels={'name':'Full Name','dob':'Date Of Birth',
        'pin':'Pin Code','mobile':'Mobile No','email':'Email ID','profile_img':'Profile Image','hscssc':'HSC/SSC','document':'Document'}
        widgets={

            'name':forms.TextInput(attrs={'class':'form-control',}),
            'dob':forms.DateInput(attrs={'class':'form-control','placeholder':'YY/MM/DD'}),
            'village':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'panchayat':forms.Select(attrs={'class':'form-select'}),
            'job_panchayat':forms.Select(attrs={'class':'form-select'}),
        }

class ServiceaForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ServiceaForm,self).__init__(*args,**kwargs)
        self.fields['service_name'].required=True
        self.fields['house_no'].required=True
        self.fields['user_name'].required=True
        self.fields['user_image'].required=True
        self.fields['firstname'].required=True
        self.fields['wardno'].required=True
        self.fields['grampanchayat'].required=True
        self.fields['phone'].required=True
        self.fields['village'].required=True
        self.fields['state'].required=True
        self.fields['pin_code'].required=True
        self.fields['adhar_no'].required=True
        self.fields['adhar_img'].required=True
        self.fields['incom_proof'].required=True
    class Meta:
        model=service_A
        fields=['income_id','service_name','house_no','user_name','user_image','firstname','lastname','email','gender','wardno','grampanchayat','phone','village','city','state','pin_code','adhar_no','adhar_img','incom_proof','vote']
        widgets={

            'service_name':forms.TextInput(attrs={'class':'form-control','value':'Income Service'}),
            'house_no':forms.NumberInput(attrs={'class':'form-control'}),
            'user_name':forms.TextInput(attrs={'class':'form-control'}),
            'user_image':forms.FileInput(attrs={'required':'True'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-select'}),
            'wardno':forms.NumberInput(attrs={'class':'form-control'}),
            'grampanchayat':forms.Select(attrs={'class':'form-select'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'village':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'pin_code':forms.NumberInput(attrs={'class':'form-control'}),
            'adhar_no':forms.NumberInput(attrs={'class':'form-control'}),
        }


class ServicecForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ServicecForm,self).__init__(*args,**kwargs)
        self.fields['name'].required=True
        self.fields['ration_no'].required=True
        self.fields['village'].required=True
        self.fields['pin'].required=True
        self.fields['mobile'].required=True
        self.fields['panchayat'].required=True
        self.fields['bpl_img'].required=True
        self.fields['adhar_img'].required=True
        self.fields['bnk_img'].required=True
        self.fields['user_img'].required=True
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    #panchayat=forms.ChoiceField(choices=PANCHAYAT,widget=forms.Select(attrs={'class':'form-control'}))
    #job_panchayat=forms.Mult
    # ipleChoiceField(label='prefered job location',choices=JOB_PANCHAYAT,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=service_C
        fields=['name','ration_no','gender','village','city','pin','state','mobile','email','panchayat','bpl_img','adhar_img','bnk_img','user_img']
        labels={'name':'Full Name','ration_no':'Ration Number',
        'pin':'Pin Code','mobile':'Mobile No','email':'Email ID','bpl_img':'BPL card Image','adhar_img':'Adhar card image','bnk_img':'PassBook Image','user_img':'applicant image'}
        widgets={

            'name':forms.TextInput(attrs={'class':'form-control',}),
            'ration_no':forms.DateInput(attrs={'class':'form-control'}),
            'village':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'panchayat':forms.Select(attrs={'class':'form-select'}),
        }


#class ApproveForm(forms.ModelForm):
   # def __init__(self,*args,**kwargs):
        #super(ApproveForm,self).__init__(*args,**kwargs)
        #self.fields['decision'].required=True
    #decision=forms.ChoiceField(choices=DECISION_CHOICE,widget=forms.RadioSelect)
    #class Meta:
        #model=approve
        #fields=['no','decision']
        #labels={'decision':'Accept/decline the applicant request',}
        #decision=forms.ChoiceField(choices=DECISION_CHOICE,widget=forms.RadioSelect)
        #widgets={
         #   'no':forms.TextInput(attrs={'class':'form-control',})
        #}
        



class ServicezForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ServicezForm,self).__init__(*args,**kwargs)
        self.fields['service_name'].required=True
        self.fields['name'].required=True
        self.fields['house_no'].required=True
        self.fields['dob'].required=True
        self.fields['gender'].required=True
        self.fields['village'].required=True
        self.fields['city'].required=True
        self.fields['pin'].required=True
        self.fields['state'].required=True
        self.fields['mobile'].required=True
        self.fields['panchayat'].required=True
        self.fields['keyno'].required=True
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    #job_panchayat=forms.Mult
    # ipleChoiceField(label='prefered job location',choices=JOB_PANCHAYAT,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=service_Z
        fields=['service_name','name','house_no','dob','gender','village','city','pin','state','mobile','email','panchayat','keyno','user_img','bpl_img','adhar_img','bnk_img','vote_img','pan_img','incm_img','cst_img','scldoc','otdc_img']
        labels={'service_name':'Service Name','name':'Applicant Name','house_no':'House Number',
        'dob':'Birth Date','gender':'Gender','village':'Your village','city':'Your City','pin':'Pin Code','state':'State','mobile':'Mobile No','email':'Email ID','panchayat':'Your Panchayat','bpl_img':'Ration card Image','keyno':'key_no','adhar_img':'Adhar card image','bnk_img':'PassBook Image','user_img':'applicant image','vote_img':'Voter ID',
        'pan_img':'Pan card','incm_img':'Income card','cst_img':'Cast certificate','scldoc':'School documents','otdc_img':'Other Documents'}
        widgets={
            'service_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter service name'}),
            'name':forms.TextInput(attrs={'class':'form-control',}),
            'house_no':forms.DateInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','placeholder':'YY/MM/DD'},),
            'gender':forms.DateInput(attrs={'class':'form-control'}),
            'village':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control','value':'karnataka'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'panchayat':forms.Select(attrs={'class':'form-select'}),
            'keyno':forms.DateInput(attrs={'class':'form-control'}),
            'bpl_img':forms.FileInput(attrs={'multiple':True}),
            'user_img':forms.FileInput(attrs={'multiple':True}),
            'adhar_img':forms.FileInput(attrs={'multiple':True}),
            'bnk_img':forms.FileInput(attrs={'multiple':True}),
            'vote_img':forms.FileInput(attrs={'multiple':True}),
            'pan_img':forms.FileInput(attrs={'multiple':True}),
            'incm_img':forms.FileInput(attrs={'multiple':True}),
            'cst_img':forms.FileInput(attrs={'multiple':True}),
            'scldoc':forms.FileInput(attrs={'multiple':True}),
            'otdc_img':forms.FileInput(attrs={'multiple':True}),
            
        }

