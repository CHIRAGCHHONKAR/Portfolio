from django.contrib import admin
from personalinfo.models import *

class personalinfo_admin(admin.ModelAdmin):
    list_display=['personal_name','personal_img']
    
class personal_links_admin(admin.ModelAdmin):
    list_display=['personal_links_logo','personal_links_link']    
    
    
admin.site.register(personalinfo,personalinfo_admin)  
admin.site.register(personal_links,personal_links_admin)
# Register your models here.
