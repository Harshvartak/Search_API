from django.db import models
from django.conf import settings

class Bank(models.Model):
    ifsc = models.TextField(blank=True)
    bank_id = models.IntegerField(blank=True, null=True)
    branch = models.TextField(blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=200,blank=True)
    district = models.TextField(blank=True)
    state = models.TextField(blank=True)
    bank_name = models.TextField(blank=True)

    def __str__(self):
        return self.ifsc
