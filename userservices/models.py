from django.core.validators import RegexValidator
from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Appoinment(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    date = models.DateField(auto_now_add=False,auto_now=False,blank=False)
    time = models.TimeField(auto_now_add=False,auto_now=False,blank=False)
    message = models.TextField('message')
    userid = models.ForeignKey(Register,on_delete=models.CASCADE)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    message = models.TextField('message')



