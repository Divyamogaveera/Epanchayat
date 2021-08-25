from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   gender = models.BooleanField(default=True)
   grampanchayat=models.CharField(default="gram",max_length=122) # True for male and False for female
   # you can add more fields here.