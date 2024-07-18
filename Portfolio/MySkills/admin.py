from django.contrib import admin
from Portfolio.MySkills.models import *

class Designadmin(admin.ModelAdmin):
    list_display=['Design_name','Design_Knowledge_percentage']
    
class Languagesadmin(admin.ModelAdmin):
    list_display=['Language_name','Languages_Knowledge_percentage']    
    
class Codingadmin(admin.ModelAdmin):
    list_display=['Coding_name','Coding_Knowledge_percentage']
    
class AllKnowledgeadmin(admin.ModelAdmin):
    list_display=['Knowledge_name']  
    
    
admin.site.register(Design,Designadmin)
admin.site.register(Languages,Languagesadmin)
admin.site.register(Coding,Codingadmin)
admin.site.register(AllKnowledge,AllKnowledgeadmin)
          
# Register your models here.
