from django.db import models
import datetime as dt   

# Create your models here.

class Location(models.Model):
    country= models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

class Image(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id )
        return image

    @classmethod
    def search_image(cls, searchterm):
        images = cls.objects.filter(category= searchterm)
        return images

    @classmethod
    def filter_image(cls, category):
        images = cls.objects.filter(category=category)
        return images
