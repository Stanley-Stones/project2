from django.db import models
from django.contrib.auth.models import User

# Create your models here.


TYPE = {
  'Apartment': 'Apartment', 
  'House': 'House',
  'Flat': 'Flat',
  'Duplex': 'Duplex',
  'Bungalow': 'Bungalow',
  'Townhouse': 'Townhouse',
  'Rooftop': 'Rooftop',
  'Building': 'Building',
  'Commercial': 'Commercial',
  'Shop': 'Shop'
}

STATUS = {
  'Rent': 'Rent',
  'Sale': 'Sale',
  'Lease': 'Lease'
}


class Location(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
      return self.name
  

class Listing(models.Model):
  host = models.CharField(max_length=255)
  property_type = models.CharField(choices=TYPE, max_length=50)
  property_status = models.CharField(choices=STATUS, max_length=50)
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='listing_images', null=True, blank=True)
  area = models.IntegerField(default='0')
  price = models.PositiveIntegerField(default='0')
  beds = models.PositiveIntegerField(default='0')
  baths = models.PositiveIntegerField(default='0')
  location = models.ForeignKey(Location, on_delete=models.CASCADE)


  def __str__(self):
      return self.title
  

class Profile(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='profile_images')
  phone = models.IntegerField()
  email = models.EmailField()
  bio = models.TextField()

  def __str__(self):
      return self.name
  