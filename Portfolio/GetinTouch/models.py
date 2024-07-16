from django.db import models



class contactdetails(models.Model):
    map=models.CharField()
    Address=models.CharField()
    Email=models.EmailField()
    Phone_num=models.CharField(blank=True)
    Freelance=models.CharField()
# Create your models here.
