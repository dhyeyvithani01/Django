from django.db import models

class Student(models.Model):
    emplyees = models.CharField(max_length=100)
    age = models.IntegerField(default=30)