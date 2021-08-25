
from os import truncate
from django import forms
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, update_last_login
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.enums import Choices
from django.db.models.manager import Manager
from django.forms import widgets
from django.forms.widgets import DateTimeInput, Widget
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin
from datetime import date, datetime, timezone
from django.utils.translation import gettext_lazy as _
from myapp.managers import CustomUserManager

#class User(AbstractUser):
   #jkusername=models.CharField(max_length=30,unique=True)
   #jkpassword=models.CharField(max_length=40)
   #jkblank=True if not required
   #email=models.EmailField(max_length=225)
   #GENDER_CHOICE=(('Male','Male'),('Female','Female'),('I prefer not to say','I prefer not to say'))
   #gender = models.CharField(max_length=20,choices=GENDER_CHOICE)#,blank=True)
   #jkuser=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
   #phone=models.IntegerField()#blank=True)
   #wardno=models.IntegerField()
   #Birth_date = models.DateField(help_text='YY-MM-DD')#,default=date.today
   #grampanchayat=models.CharField(max_length=40,help_text='Enter your panchayat')#,blank=True)
   
   #USERNAME_FIELD='username'
   #REQUIRED_FIELDS=['email','gender','phone','wardno','Birth_date','grampanchayat']
   #objects=CustomUserManager()
   #objects=CustomUserManager()

class User(AbstractBaseUser,PermissionsMixin):
   user_id=models.AutoField(primary_key=True) 
   username=models.CharField(max_length=30,unique=True)
   first_name=models.CharField(max_length=150)
   last_name=models.CharField(max_length=150,blank=True)
   #start_date=models.DateTimeField()
   date_joined=models.DateTimeField(default=datetime.now)
   #password=models.CharField(max_length=40)
   #blank=True if not required
   email=models.EmailField(_('email address'),max_length=225,unique=True)
   GENDER_CHOICE=(('Male','Male'),('Female','Female'),('I prefer not to say','I prefer not to say'))
   gender = models.CharField(max_length=20,choices=GENDER_CHOICE)#,blank=True)
   #user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
   phone=models.IntegerField()#blank=True)
   wardno=models.IntegerField()
   Birth_date = models.DateField(help_text='YY-MM-DD',blank=True)
   grampanchayat=models.CharField(max_length=40,help_text='Enter your panchayat',)
   is_staff=models.BooleanField(default=False)
   is_active=models.BooleanField(default=True)
 

   objects=CustomUserManager()
   
   USERNAME_FIELD='username'
   REQUIRED_FIELDS=['email','first_name','last_name','gender','phone','wardno','Birth_date','grampanchayat']
   
   
   def __str__(self):
       return self.username
    # True for male and False for female
   # you can add more fields here.


# Create your models here.
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    name= models.CharField(max_length=122)
    email=models.EmailField(max_length=250)
    GENDER_CHOICE=(('Male','Male'),('Female','Female'),('I prefer not to say','I prefer not to say'))
    gender = models.CharField(max_length=20,choices=GENDER_CHOICE)#,blank=True)
    phone=models.CharField(max_length=12)
    grampanchayat=models.CharField(max_length=50)
    wardno=models.IntegerField(default=0)
    info=models.TextField()
    adinfo=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name

class Feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    name= models.CharField(max_length=122)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=12)
    wardno=models.IntegerField(default=0)
    grampanchayat=models.CharField(max_length=50)
    rate=models.TextField()
    adinfo=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name

class Complaints(models.Model):
    complaints_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    firstname= models.CharField(max_length=122)
    lastname=models.CharField(max_length=250)
    email=models.EmailField(max_length=30)
    GENDER_CHOICE=(('Male','Male'),('Female','Female'),('I prefer not to say','I prefer not to say'))
    gender = models.CharField(max_length=20,choices=GENDER_CHOICE,blank=True)
    wardno=models.IntegerField(default=0)
    grampanchayat=models.CharField(max_length=40,blank=True)
    complaint=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.firstname
        
#class UserProfile(models.Model):
    #pass
    #user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    #phone=models.IntegerField(blank=True,default=0)
    #wardno=models.IntegerField(blank=True,default=0)
    #Birth_date = models.DateField() 
    #grampanchayat=models.CharField(blank=True,max_length=50,default='some string')

    #def __str__(self) -> str:
        #return self.user
        

    #def __str__(self) -> str:
        #return super(User).__str__(User)

#class UserManager(BaseUserManager):

#service
class service(models.Model):
    service_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    service_name=models.CharField(max_length=50,unique=True,blank=True)
    description=models.CharField(max_length=100,blank=True)
    requirements=models.CharField(max_length=300,blank=True)
    #service_req_id=models.ForeignKey(service_req_id,on_delete=models.CASCADE)
    #user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name

class service_A(models.Model):
    ration_id=models.AutoField(primary_key=True)
    service_id=models.ForeignKey(service,on_delete=models.PROTECT,default="1")
    user=models.ForeignKey(User,on_delete=models.PROTECT,default="",null=True)
    service_name=models.CharField(max_length=50,blank=True)
    user_name=models.CharField(max_length=100,default="")
    user_image=models.FileField(blank=True,upload_to="images/")
    firstname= models.CharField(max_length=122)
    lastname=models.CharField(max_length=250,blank=True)
    email=models.EmailField(max_length=30)
    GENDER_CHOICE=(('Male','Male'),('Female','Female'),('I prefer not to say','I prefer not to say'))
    gender = models.CharField(max_length=20,choices=GENDER_CHOICE,blank=True)
    wardno=models.IntegerField(default=0)
    GRAM_CHOICE=(('Aloor','Aloor'),('Harkur','Harkur'))
    grampanchayat=models.CharField(max_length=40,blank=True,choices=GRAM_CHOICE)
    phone=models.CharField(null=True,max_length=12)
    village=models.CharField(_("address"), max_length=150)
    city=models.CharField(_("city"), max_length=100,default="kundapura")
    STATE_CHOICE=(('KARNATAKA','KARNATAKA'),('TAMILNADU','TAMILNADU'))
    state=models.CharField(choices=STATE_CHOICE,max_length=50)
    pin_code=models.CharField(_("pin_code"),max_length=100)
    adhar_no=models.CharField(max_length=12,default="")
    adhar_img=models.FileField(upload_to="images/",blank=True)
    incom_proof=models.FileField(upload_to="images/",default="")
    vote=models.FileField(upload_to="images/",default="")
    apply_date=models.DateField(null=True)

    def __str__(self):
        return self.service_name


STATE_CHOICE=(
    ('karnataka','karnataka'),
    ('andrapradesh','andrapradesh')
)
PANCHAYAT=(
    ('aloor','aloor'),
    ('kota','kota')
)
JOB_PANCHAYAT=(
    ('Aloor','Aloor'),
    ('Kota','Kota'),
    ('Andrapradesh','Andrapradesh')
)
GENDER_CHOICE=(
    ('MAKE','MALE'),
    ('FEMALE','FEMALE'),
    ('OTHERS','OTHERS')
)
class Service_B(models.Model):
    name = models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=50,choices=GENDER_CHOICE)
    village=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    panchayat=models.CharField( choices=PANCHAYAT,max_length=100)
    job_panchayat=models.CharField(choices=JOB_PANCHAYAT,max_length=100)
    profile_img=models.ImageField(upload_to='profileimg',blank=True)
    document=models.FileField(upload_to='doc',blank=True)

class service_C(models.Model):
    name = models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=50,choices=GENDER_CHOICE)
    village=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    panchayat=models.CharField(choices=PANCHAYAT,max_length=100)
    

class imgsall(models.Model):
    allimg=models.ImageField(upload_to='allimg',blank=True)
    document=models.FileField(upload_to='document',blank=True)


    






    