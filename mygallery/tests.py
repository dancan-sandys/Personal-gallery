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

    def test_deleting(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images),0)

    # def test_update(self):
        
    #     self.new_image.update_image(id = self.new_image.id ,name = 'Dancan'")

    def test_get_image_by_id(self):
        id = 1
        image = Image.get_image_by_id(id)
        self.assertTrue(len(image)==0)

    def test_search_image(self):
        Category = self.new_category
        image = Image.search_image(Category)
        self.assertTrue(len(image)==0)

    def test_filter_image(self):
        Category = self.new_category
        image = Image.filter_image(Category)
        self.assertTrue(len(image)==0)