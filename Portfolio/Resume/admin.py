from django.contrib import admin
from Resume.models import *

class resumeadmin(admin.ModelAdmin):
    list_display=['School_or_University_name','Degree_or_Diploma_name','Passing_Year']
    
admin.site.register(resume,resumeadmin)    
# Register your models here.
