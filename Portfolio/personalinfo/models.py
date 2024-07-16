from django.db import models



class personalinfo(models.Model):
    personal_img=models.ImageField(upload_to='personal_info')
    personal_name=models.CharField()
    
class personal_links(models.Model):
    personal_links_logo=models.CharField()
    personal_links_link=models.CharField()
# Create your models here.
