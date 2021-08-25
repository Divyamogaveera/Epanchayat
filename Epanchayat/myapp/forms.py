
from django.contrib.auth import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import GENDER_CHOICE, JOB_PANCHAYAT, User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User,service,Contact,Service_B
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
        fields = ['username','first_name','last_name','email','gender','Birth_date','phone','wardno','grampanchayat']
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
    ('Andrapradesh','Andrapradesh')
)
class ServicebForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect)
    #job_panchayat=forms.MultipleChoiceField(label='prefered job location',choices=JOB_PANCHAYAT,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Service_B
        fields=['name','dob','gender','village','city','pin','state','mobile','email','panchayat','job_panchayat','profile_img','document']
        labels={'name':'Full Name','dob':'Date Of Birth',
        'pin':'Pin Code','mobile':'Mobile No','email':'Email ID','profile_img':'Profile Image','document':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'village':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'panchayat':forms.Select(attrs={'class':'form-select'}),
            'job_panchayat':forms.Select(attrs={'class':'form-select'}),
        }