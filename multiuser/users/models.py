from django.contrib.auth.models import AbstractUser
from django.db import models
import random

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    role=models.CharField(max_length=20)

    # # otp=models.CharField(max_length=11,null=True)
    # is_verified=models.BooleanField(default=False)

    # def generate_otp(self):
    #     otp=str(random.randint(1000,9999))+str(self.id)
    #     self.otp=otp
    #     self.save()
