from django.db import models


class resume(models.Model):
    School_or_University_name=models.CharField()
    Degree_or_Diploma_name=models.CharField()
    Passing_Year=models.CharField()
# Create your models here.
