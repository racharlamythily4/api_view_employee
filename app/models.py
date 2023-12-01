from django.db import models

# Create your models here.
class Employee(models.Model):
    Ename=models.CharField(max_length=100)
    Esal=models.IntegerField()
    Ejob=models.CharField(max_length=100)

