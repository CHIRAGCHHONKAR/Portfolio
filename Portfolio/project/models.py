from django.db import models


# Banner works
class Banner(models.Model):
    Banner_id=models.CharField(max_length=100,default=None)
    Banner_img=models.FileField(upload_to='Projects/Banner',default=None)
    Banner_title=models.CharField(max_length=100)
    
# Socialmedia Post works
class Socialmedia_Post(models.Model):
    Socialmedia_Post_id=models.CharField(max_length=100,default=None)
    Socialmedia_Post_img=models.FileField(upload_to='Projects/Post',default=None)
    Socialmedia_Post_title=models.CharField(max_length=100)
    
# Manipulation works
class Manipulation(models.Model):
    Manipulation_id=models.CharField(max_length=100,default=None)
    Manipulation_img=models.FileField(upload_to='Projects/Manipulation',default=None)
    Manipulation_title=models.CharField(max_length=100)
    
# Web Development Works 
class Web_Development(models.Model):
    Web_Development_id=models.CharField(max_length=100,default=None)
    Web_Development_img=models.FileField(upload_to='Projects/Web_Development',default=None)
    Web_Development_title=models.CharField(max_length=100)      
    Web_Development_Link=models.CharField(max_length=2000)      
# Create your models here.
