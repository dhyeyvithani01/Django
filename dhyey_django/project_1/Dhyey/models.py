from django.db import models
from datetime import datetime
from django.utils import timezone
from django_countries.fields import CountryField

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField(default=30)
    Email_id = models.EmailField(max_length=30)
    Mobile_no = models.CharField(max_length=10)
    Address = models.TextField(max_length=100)
    Password =models.CharField(max_length=100)
    Confirm_password =models.CharField(max_length=100)
    Date=models.DateTimeField(default=timezone.now)
    Time=models.TimeField(default=timezone.now)
    Birth_Date=models.DateField(default=datetime.now)
    Country=CountryField(null=True)

# class Teacher(models.Model):
#     name = models.CharField(max_length=100)
#     subjects = models.CharField(max_length=20)
