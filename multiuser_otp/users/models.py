from django.contrib.auth.models import AbstractUser
from django.db import models
import random

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    role=models.CharField(max_length=20)

    # otp and otp verification
    otp=models.CharField(max_length=11,null=True) # to store otp in backend table
    is_verified=models.BooleanField(default=False) # to check whether user is otp verified or not

    def generate_otp(self):
        otp=str(random.randint(1000,9999))+str(self.id) # 5 digit otp
        self.otp=otp # stores the otp in User table
        self.save()


