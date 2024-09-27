from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dob=models.CharField(max_length=100)
    aadhar_no=models.IntegerField()
    mobile_no=models.IntegerField()