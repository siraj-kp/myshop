from django.db import models
from PIL import Image

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.ImageField(default='default.jpg', upload_to='product_pics')


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=600)
    city = models.CharField(max_length=255)
    phone = models.IntegerField()
    total = models.CharField(max_length=300)
    item_name = models.CharField(max_length=255)







