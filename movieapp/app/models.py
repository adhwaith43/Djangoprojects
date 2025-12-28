from django.db import models

class Movie(models.Model):
    image=models.ImageField(upload_to='movies')
    moviename=models.CharField(max_length=50)
    description=models.TextField()
    director=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    year=models.IntegerField
# Create your models here.
