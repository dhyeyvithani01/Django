from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField(default=30)
    Email_id = models.EmailField(max_length=30)
    Mobile_no = models.CharField(max_length=10)
    Address = models.TextField(max_length=100)


# class Teacher(models.Model):
#     name = models.CharField(max_length=100)
#     subjects = models.CharField(max_length=20)
