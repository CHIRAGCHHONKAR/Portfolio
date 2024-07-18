from django.contrib import admin
from Portfolio.Services.models import *

class service_admin(admin.ModelAdmin):
    list_display=['service_id','services_title','services_description','services_logo']
    
admin.site.register(service,service_admin)    
# Register your models here.
