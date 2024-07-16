from django.contrib import admin
from project.models import *


class Banner_admin(admin.ModelAdmin):
    list_display=['Banner_id','Banner_title','Banner_img']

class Socialmedia_Post_admin(admin.ModelAdmin):
    list_display=['Socialmedia_Post_id','Socialmedia_Post_title','Socialmedia_Post_img']    
    
class Manipulation_admin(admin.ModelAdmin):
    list_display=['Manipulation_id','Manipulation_title','Manipulation_img']        
    
class Web_Development_admin(admin.ModelAdmin):
    list_display=['Web_Development_id','Web_Development_title','Web_Development_Link','Web_Development_img']    
    
    
    
admin.site.register(Banner,Banner_admin)
admin.site.register(Socialmedia_Post,Socialmedia_Post_admin)
admin.site.register(Manipulation,Manipulation_admin)
admin.site.register(Web_Development,Web_Development_admin)    
# Register your models here.
