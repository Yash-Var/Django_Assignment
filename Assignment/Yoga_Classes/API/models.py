from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=30, blank=False)
    age = models.IntegerField(blank=False)
    # doj = models.DateField(blank=False)
    # batchType = models.TextChoices('BatchType', '6-7AM 7-8AM 8-9AM 5-6PM')
    # paymentStatus = models.BooleanField(default=False)