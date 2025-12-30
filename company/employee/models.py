from django.db import models

# Create your models here.

# Table Definition
class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField()
    deptname=models.CharField(max_length=20)
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    image=models.ImageField(upload_to='employeeimg')
