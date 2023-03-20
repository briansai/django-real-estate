from django.db import models

# Create your models here.
class Listing(models.Model):
      title = models.CharField(max_length=150)
      price = models.IntegerField()
      num_bedrooms = models.IntegerField() 
      num_bathrooms = models.IntegerField()
      sq_foot = models.IntegerField()
      address = models.CharField(max_length=100)
      # image
