from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from .models import Complaints, Contact, Feedback ,service,service_A,Service_B,service_C,service_Z,approve1,approve2,approve3,approve4
from myapp.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm



class CustomUserAdmin(UserAdmin):
    add_form=UserCreationForm
    form=UserChangeForm
    model=User
    list_display=['username','first_name','wardno','grampanchayat']
    add_fieldsets=UserAdmin.add_fieldsets + (
        (None,{'fields':('email','first_name','last_name','gender','Birth_date','phone','wardno','grampanchayat')}),
    )
    fieldsets=UserAdmin.fieldsets + (
        (None,{'fields':('gender','Birth_date','phone','wardno','grampanchayat')}),
    )

    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
        #if db_field.name=='user':kwargs['queryset']=User.objects.filter(user=request.user) 
        #return super().formfield_for_foreignkey(user, request, **kwargs)

#from django.conf import settings
#User = settings.AUTH_USER_MODEL
#class CustomUserCreationForm(UserCreationForm):

    #class Meta(UserCreationForm.Meta):
        #model =User
        #fields =UserCreationForm.Meta.fields+('phone',)

#class CustomUserAdmin(ModelAdmin):
    #form=CustomUserCreationForm

#class MyUserChangeForm(UserChangeForm):
    #class Meta(UserChangeForm.Meta):
        #model = User

#class MyUserAdmin(UserAdmin):
    #model = User
    # add_fieldsets = UserAdmin.fieldsets + ((None, {'personalinfo': ('phone',)}),)

# Register your models here.
admin.site.register(User,CustomUserAdmin)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Complaints)
#admin.site.register(UserProfile)
#admin.site.register(service)
#admin.site.register(service_A)


@admin.register(approve1)
class approve(admin.ModelAdmin):
    list_display=['app_id','income_no','decision']

@admin.register(approve2)
class approve(admin.ModelAdmin):
    list_display=['app_id','job_no','decision']

@admin.register(approve3)
class approve(admin.ModelAdmin):
    list_display=['app_id','gas_no','decision']

@admin.register(approve4)
class approve(admin.ModelAdmin):
    list_display=['app_id','curr_no','decision']


@admin.register(service)
class service(admin.ModelAdmin):
    list_display=['service_name']

@admin.register(service_A)
class ServiceA(admin.ModelAdmin):
    list_display=['house_no','servicea_id','user_image','grampanchayat','apply_date']

@admin.register(Service_B)
class ServiceB(admin.ModelAdmin):
    list_display=['job_id','name','dob','gender','village',
    'panchayat','pin','job_panchayat','profile_img',]

@admin.register(service_C)
class ServiceC(admin.ModelAdmin):
    list_display=['gas_id','servicec_id','user','ration_no',
    'panchayat','bpl_img',]

@admin.register(service_Z)
class ServiceZ(admin.ModelAdmin):
    list_display=['curr_id','keyno','service_name','panchayat',]








