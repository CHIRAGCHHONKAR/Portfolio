from django.db import models


class Contactform(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
# Create your models here.
