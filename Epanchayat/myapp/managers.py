from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _, ugettext_lazy
from django.contrib.auth.models import BaseUserManager

#class CustomUsermanager(BaseUserManager):
    
    #def create_user(self, username, password )
    #    if not username:
            #raise ValueError(('the username must be set'))
#class CustomUserManager(models.Manager):
    #def get_queryset(self):
        #return super().get_queryset().all()

class CustomUserManager(BaseUserManager):

    def create_superuser(self,username,password,first_name,last_name,email,gender,phone,wardno,Birth_date,grampanchayat,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff')is not True:
            raise ValueError('superuser must be asigned to is_staff=True')
        if other_fields.get('is_superuser')is not True:
            raise ValueError('superuser must be asigned to is_superuser=True.')

        return self.create_user(username,password,first_name,last_name,email,gender,phone,wardno,Birth_date,grampanchayat,**other_fields)


    def create_user(self,username,password,first_name,last_name,email,gender,phone,wardno,Birth_date,grampanchayat,**other_fields):

        if not username:
            raise ValueError(_('you must provide username'))

        email=self.normalize_email(email)#lowercase
        user=self.model(username=username,first_name=first_name,last_name=last_name,gender=gender,phone=phone,Birth_date=Birth_date,grampanchayat=grampanchayat,wardno=wardno,**other_fields)
        user.set_password(password)
        user.save()
        return user

    