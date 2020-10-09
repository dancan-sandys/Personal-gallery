from django.test import TestCase
from .models import Image, Location,Category
# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):
        self.new_category = Category(name='Family')
        self.new_location = Location(country='Kenya',city='Kisumu')
        self.new_category.save_category()
        self.new_location.save_location()
        self.new_image = Image(name='Sandys',description='Yes',location= self.new_location, category=self.new_category) 

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_saving(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)