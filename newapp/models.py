from django.db import models

# Create your models here.
class Reg(models.Model):
    fristname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
    mobileno=models.IntegerField()
    emailid=models.EmailField()