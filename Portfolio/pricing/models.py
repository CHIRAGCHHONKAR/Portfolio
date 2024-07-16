from django.db import models

class Price(models.Model):
    plan_logo = models.CharField(max_length=50)
    plan_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    services = models.TextField(help_text="Enter services separated by commas")
    purchase = models.CharField(max_length=100)

    def __str__(self):
        return self.plan_name
