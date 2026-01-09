from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    role=models.CharField(max_length=20)

class School(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)