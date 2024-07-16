from django.db import models


class service(models.Model):
    service_id=models.CharField(default=None)
    services_logo=models.CharField()
    services_title=models.CharField()
    services_description=models.TextField()
# Create your models here.
