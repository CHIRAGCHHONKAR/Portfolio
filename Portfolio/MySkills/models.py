from django.db import models


class Design(models.Model):
    Design_name=models.CharField()
    Design_Knowledge_percentage=models.CharField()
    
class Languages(models.Model):
    Language_name=models.CharField()
    Languages_Knowledge_percentage=models.CharField() 
    
class Coding(models.Model):
    Coding_name=models.CharField()
    Coding_Knowledge_percentage=models.CharField()
    
class AllKnowledge(models.Model):
    Knowledge_name=models.CharField()    
           
# Create your models here.
