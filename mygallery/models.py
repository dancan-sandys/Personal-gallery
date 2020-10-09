from django.db import models
import datetime as dt   

# Create your models here.

class Location(models.Model):
    country= models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=30)

class Image(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)


