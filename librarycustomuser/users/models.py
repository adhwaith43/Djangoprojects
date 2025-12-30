from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customuser(AbstractUser):
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=11)
    gender=models.CharField(max_length=11)
