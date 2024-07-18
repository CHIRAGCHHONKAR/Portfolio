from django.contrib import admin
from Aboutme.models import *

class bioadmin(admin.ModelAdmin):
    list_display=['Bio']

class infoadmin(admin.ModelAdmin):
    list_display=['Age','Residence','Freelance','Address']    
    
admin.site.register(bio,bioadmin)
admin.site.register(info,infoadmin)    
# Register your models here.
