from django.contrib import admin
from Portfolio.contactform.models import *

class Contactformadmin(admin.ModelAdmin):
    list_display=['name','email','message']

admin.site.register(Contactform,Contactformadmin)    
# Register your models here.
