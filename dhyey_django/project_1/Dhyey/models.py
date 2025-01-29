from django.db import models

class Employers(models.Model):
    emplyees = models.CharField(max_length=100)
    age = models.IntegerField(default=30)