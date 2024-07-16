from django.db import models


class bio(models.Model):
    Bio=models.TextField()
    
class info(models.Model):
    Age=models.IntegerField()
    Residence=models.CharField(max_length=50)
    Freelance=models.CharField()
    Address=models.CharField()
# Create your models here.
