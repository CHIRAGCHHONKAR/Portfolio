from django.contrib import admin
from GetinTouch.models import *

class contactdetailsadmin(admin.ModelAdmin):
    list_display=['Address','Email','Phone_num','Freelance','map']
    
    
admin.site.register(contactdetails,contactdetailsadmin)    
# Register your models here.
