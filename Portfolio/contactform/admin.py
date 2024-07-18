from django.contrib import admin
from contactform.models import *

class Contactformadmin(admin.ModelAdmin):
    list_display=['name','email','message']

admin.site.register(Contactform,Contactformadmin)    
# Register your models here.
